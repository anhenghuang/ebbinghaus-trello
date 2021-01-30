from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from trello import TrelloClient, trellolist
from utils import get_memo_lists, get_memo_cards

class Ebbinghaus(object):
    client = None
    board_name = ''
    list_completed_name = ''
    list_review_name = ''
    list_memory_name = ''

    def __init__(self, api_key, api_secret, token, token_secret,
                 board_name='trello-memo-board',
                 list_completed_name='complete',
                 list_review_name='review',
                 list_memory_name='memory'):
        self.client = TrelloClient(
            api_key=api_key,
            api_secret=api_secret,
            token=token,
            token_secret=token_secret
        )
        self.board_name = board_name
        self.list_completed_name = list_completed_name
        self.list_review_name = list_review_name
        self.list_memory_name = list_memory_name
        self.check_connect()

    def check_connect(self):
        list_completed, list_review, list_memory = get_memo_lists(
            self.client, self.board_name, self.list_completed_name, self.list_review_name, self.list_memory_name)
        if isinstance(list_completed, trellolist.List) \
               and isinstance(list_review, trellolist.List) \
               and isinstance(list_memory, trellolist.List):
            print('connect success', list_completed, list_review, list_memory)
        else:
            raise ValueError('check_connect failed')

    def is_need_review(self, trello_card):
        """
        check if the card need review based on the 'memo' tag in comments
        """
        times_now = 0
        last_date = "1990-01-01"
        td = datetime.today().strftime("%Y-%m-%d")
        for comment in trello_card.get_comments():
            txt = comment.get("data", {}).get("text", "")
            if "memo:" in txt:
                _, times, pt = txt.split(":")
                times_now = max(int(times), times_now)
                last_date = max(last_date, pt)
        if times_now == 0:
            return False
        else:
            next_review_date = datetime.strptime(last_date, "%Y-%m-%d") + timedelta(days=2 ** times_now)
            if td == next_review_date.strftime("%Y-%m-%d"):
                return True
            else:
                return False

    def update_memo_label(self, trello_card):
        times = 0
        for comment in trello_card.get_comments():
            txt = comment.get("data", {}).get("text", "")
            if "memo:" in txt:
                times = max(times, int(txt.split(":")[1]))
        trello_card.comment(
            "memo:" + str(times + 1) + ":" + datetime.today().strftime("%Y-%m-%d")
        )

    def check_review(self):
        list_completed, list_review, list_memory = get_memo_lists(
            self.client, self.board_name, self.list_completed_name, self.list_review_name, self.list_memory_name)
        for card in get_memo_cards(list_memory):
            if self.is_need_review(card):
                card.change_list(list_review.id)

    def check_completed(self):
        list_completed, list_review, list_memory = get_memo_lists(
            self.client, self.board_name, self.list_completed_name, self.list_review_name, self.list_memory_name)
        for card in get_memo_cards(list_completed):
            self.update_memo_label(card)
            card.change_list(list_memory.id)

    def run_scheduler(self,
                      check_completed_hour=23, check_completed_minute=30,
                      check_review_hour=0, check_review_minute=30):
        scheduler = BlockingScheduler()
        scheduler.add_job(self.check_completed, 'cron', hour=check_completed_hour, minute=check_completed_minute)
        scheduler.add_job(self.check_review, 'cron', hour=check_review_hour, minute=check_review_minute)
        scheduler.start()


if __name__ == '__main__':
    from config import *
    ebb = Ebbinghaus(api_key=api_key,
                     api_secret=api_secret,
                     token=token,
                     token_secret=token_secret,
                     board_name=board_name,
                     list_completed_name=list_completed_name,
                     list_review_name=list_review_name,
                     list_memory_name=list_memory_name)
    ebb.run_scheduler()

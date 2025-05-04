import ptbot
from dotenv import load_dotenv
import os
from pytimeparse import parse


def wait(author_id, message):
    seconds = parse(message)
    message_id = bot.send_message(author_id, f"Осталось секунд {seconds}")
    bot.create_countdown(seconds, notify_progress, author_id=author_id,
                         message_id=message_id, total=seconds)
    bot.create_timer(seconds, shutdown, author_id=author_id)


def shutdown(author_id):
    bot.send_message(author_id, "Время вышло!")


def notify_progress(secs_left, author_id, message_id, total):
    progress_bar = render_progressbar(total, total - secs_left)
    bot.update_message(author_id, message_id, f"Осталось секунд: {secs_left}\n{progress_bar}")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    load_dotenv()
    TG_TOKEN = os.getenv("TG_TOKEN")
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(wait)
    bot.run_bot()


if __name__ == '__main__':
    main()


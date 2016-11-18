#encoding:utf-8

import os

from utils import get_url, download_file, telegram_autoplay_limit


subreddit = 'gifs'
t_channel = '@r_gifs'


def send_post(submission, r2t):
    what, gif_url, ext = get_url(submission)
    if what != 'gif':
        return False

    title = submission.title
    link = submission.short_link

    if submission.over_18:
        url = submission.url
        text = 'NSFW\n{}\n{}\n\n{}\n\nby @r_gifs'.format(url, title, link)
        return r2t.sent_text(text, disable_web_page_preview=True)

    text = '{}\n{}\n\nby @r_gifs'.format(title, link)
    return r2t.send_gif(gif_url, ext, text)

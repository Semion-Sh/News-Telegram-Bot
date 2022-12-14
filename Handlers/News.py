import asyncio, aioschedule
from create_bot import bot, dp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import os
from aiogram import types
import time
from Keyboards.News_kb import inline_kb
from .Errors import *
from Config import *

live = 'LIVE'


async def news_by_bbc_russian_big():
    for news in russian_links['bbc_russian']:
        try:
            driver.get(russian_links['bbc_russian'][news]['link'])
            last_news = driver.find_element(By.CLASS_NAME, 'bbc-mhiwdf')
            last_new_views = {
                'image': last_news.find_element(By.TAG_NAME, 'img').get_attribute('src'),
                'title': last_news.find_element(By.TAG_NAME, 'span').text,
            }
            if 'LIVE' in last_new_views['title']:
                last_new_views['title'] = live + last_new_views['title'][10:]
                driver.find_element(By.CLASS_NAME, 'bbc-mhiwdf').click()
                qa = driver.find_element(By.CLASS_NAME, 'qa-post-body').text
                if len(qa) > 1024 - len(last_new_views['title']):
                    q = 1024 - len(last_new_views['title']) - 3
                    last_new_views['text'] = qa[:q]
                else:
                    last_new_views['text'] = qa
            else:
                driver.find_element(By.CLASS_NAME, 'bbc-mhiwdf').click()
                last_new_views['text'] = driver.find_element(By.CLASS_NAME, 'bbc-19j92fr').text
            if russian_links['bbc_russian'][news]['the_last_news'] == last_new_views['image']:
                pass
            else:
                await bot.send_photo(chat_id=chennels_id['admin'],
                                     photo=last_new_views['image'],
                                     caption=f'<b>{last_new_views["title"]}</b>\n \n{last_new_views["text"]}',
                                     reply_markup=inline_kb,
                                     parse_mode='html')
                russian_links['bbc_russian'][news]['the_last_news'] = last_new_views['image']
        except Exception as e:
            await send_error(f"{russian_links['bbc_russian'][news]['link']} big {e.args}")


async def news_by_bbc_russian_war():
try:
    driver.get(russian_links['bbc_russian'])
    last_news = driver.find_element(By.CLASS_NAME, 'bbc-1tx9q9n')

    last_new_view = {
        'image': last_news.find_element(By.TAG_NAME, 'img').get_attribute('src'),
        'title': last_news.find_element(By.TAG_NAME, 'span').text,
        'text': last_news.find_element(By.TAG_NAME, 'p').get_attribute("textContent"),
    }

    if the_published_news_by_bbc_russian_1 == last_new_view['image']:
        return False
    await bot.send_photo(chat_id=chennels_id['admin'],
                        photo=last_new_view['image'],
                        caption=f'<b>{last_new_view["title"]}</b>\n \n{last_new_view["text"]}',
                        reply_markup=inline_kb,
                        parse_mode='html')
    the_published_news_by_bbc_russian_1 = last_new_view['image']
except:
    await send_error(f'{russian_links["bbc_russian"]}')


async def news_by_moscowtimes_news_big_full():
    for news in russian_links['moscowtimes']:
        try:
            driver.get(russian_links['moscowtimes'][news]['link'])
            last_news = driver.find_element(By.CLASS_NAME, 'col-12-sm')
            if news == 'moscowtimes_opinion':
                last_news.click()
                col = driver.find_element(By.CLASS_NAME, 'col')
                last_new_view = {
                    'image': col.find_element(By.CLASS_NAME, 'article__featured-image').find_element(By.TAG_NAME,
                                                                                                     'img').get_attribute(
                        'src'),
                    'title': col.find_element(By.CLASS_NAME, 'article__header').find_element(By.TAG_NAME, 'h1').text
                }
                intro = col.find_element(By.CLASS_NAME, 'article__intro').text
                last_new_view['text'] = intro + driver.find_element(By.CLASS_NAME, 'article__content').text
            else:
                last_new_view = {
                    'image': last_news.find_element(By.TAG_NAME, 'img').get_attribute('src'),
                    'title': last_news.find_element(By.TAG_NAME, 'span').text
                }
                last_news.click()
                last_new_view['text'] = driver.find_element(By.CLASS_NAME, 'article__content').text
            if russian_links['moscowtimes'][news]['the_last_news'] == last_new_view['image']:
                pass
            else:
                x = 1024 - len(last_new_view["title"]) - 3
                success_send = await bot.send_photo(chat_id=chennels_id['admin'],
                                                    photo=last_new_view['image'],
                                                    caption=f'<b>{last_new_view["title"]}</b>\n \n{last_new_view["text"][:x]}',
                                                    parse_mode='html')
                if len(last_new_view["text"][x:]) > 4096:
                    x_1 = 4096 - x
                    success_send_end = await bot.send_message(chat_id=chennels_id['admin'],
                                                              text=last_new_view["text"][x:x_1])
                else:
                    success_send_end = await bot.send_message(chat_id=chennels_id['admin'],
                                                              text=last_new_view["text"][x:])
                if len(last_new_view["title"]) + len(last_new_view["text"]) > 1024:
                    success_send
                    success_send_end
                    russian_links['moscowtimes'][news]['the_last_news'] = last_new_view['image']
                else:
                    await bot.send_photo(chat_id=chennels_id['admin'],
                                         photo=last_new_view['image'],
                                         caption=f'<b>{last_new_view["title"]}</b>\n \n{last_new_view["text"][:x]}',
                                         reply_markup=inline_kb,
                                         parse_mode='html')
                    russian_links['moscowtimes'][news]['the_last_news'] = last_new_view['image']
        except Exception as e:
            if '.article__featured-image' in e.args[0].replace(char, ' '):
                pass
            else:
                await send_error(f"""{russian_links['moscowtimes'][news]['link']} {e.args[0].replace(char, ' ')}""")


async def news_by_meduza_war():
    global the_published_news_by_bbc_russian_10
    try:
        driver.get(russian_links['meduza_war'])
        last_news = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div/div/div/section/div[1]/div[1]')
        print(last_news.text)
        last_new_view = {
            'image': last_news.find_element(By.TAG_NAME, 'img').get_attribute('src'),
            'title': last_news.find_element(By.TAG_NAME, 'span').text
        }
        driver.find_element(By.CLASS_NAME, 'col-12-sm').click()
        last_new_view['text'] = driver.find_element(By.CLASS_NAME, 'article__content').text
        if the_published_news_by_bbc_russian_10 == last_new_view['image']:
            return False
        x = 1024 - len(last_new_view["title"]) - 3
        await bot.send_photo(chat_id=chennels_id['admin'],
                             photo=last_new_view['image'],
                             caption=f'<b>{last_new_view["title"]}</b>\n \n{last_new_view["text"][:x]}',
                             reply_markup=inline_kb,
                             parse_mode='html')
        await bot.send_message(chat_id=chennels_id['admin'],
                               text=last_new_view["text"][x:])
        the_published_news_by_bbc_russian_10 = last_new_view['image']
    except Exception as e:
        await send_error(f"""{russian_links['meduza_war']}
        {e.args}""")


news_by_rambler_list = ['Ura.Ru', 'News.ru']


async def news_by_rambler():
        try:
            driver.get(russian_links['rambler']['link'])
            last_news = driver.find_element(By.CLASS_NAME, '_2bIZW')
            last_news.click()
            driver.get('https://news.rambler.ru/army/49631828-chlen-sovfeda-pokazal-video-s-zhelayuschimi-krovi-vragov-mobilizovannymi/')
            driver.find_element(By.CLASS_NAME, '_3RZvW').find_element(By.TAG_NAME, 'img').get_attribute('src')
            last_new_view = {
                'image': driver.find_element(By.CLASS_NAME, '_3RZvW').find_element(By.TAG_NAME, 'img').get_attribute('src'),
                'title': driver.find_element(By.ID, 'headline').text,
                'text': driver.find_element(By.CLASS_NAME, '_3RZvW').text
            }
            if russian_links['rambler']['the_last_news'] == last_new_view['image']:
                pass
            else:
                index = last_new_view['text'].find('News.ru')
                await bot.send_photo(chat_id=chennels_id['admin'],
                                    photo=last_new_view['image'],
                                    caption=f'<b>{last_new_view["title"]}</b>\n \n{last_new_view["text"][:index]}',
                                    parse_mode='html')
                russian_links['rambler']['the_last_news'] = last_new_view['image']
                last_new_view = {
                    'title': driver.find_element(By.ID, 'headline').text,
                    'text': driver.find_element(By.CLASS_NAME, '_3RZvW').text
                }
                print('ok')
                driver.get('driver.find_element(By.CLASS_NAME, "_3RZvW").find_element(By.CLASS_NAME, "_1ODYE").find_element(By.TAG_NAME, "iframe").get_property("src")'),
                last_new_view['video'] = driver.find_element(By.TAG_NAME, 'video').get_attribute('src')
                print(last_new_view['video'])
                if russian_links['rambler']['the_last_news'] == last_new_view['video']:
                    pass
                else:
                    index = last_new_view['text'].find('News.ru')
                    await bot.send_video(chat_id=chennels_id['admin'],
                                         video=last_new_view['video'],
                                         caption=f'<b>{last_new_view["title"]}</b>',
                                         parse_mode='html')
                    russian_links['rambler']['the_last_news'] = last_new_view['video']
        except Exception as e:
            pass
            await send_error(f"""{russian_links['rambler']['link']} {e.args[0].replace(char, ' ')}""")
        driver.get('https://news.rambler.ru/army/49631828-chlen-sovfeda-pokazal-video-s-zhelayuschimi-krovi-vragov-mobilizovannymi/')
        last_new_view = {
             'title': driver.find_element(By.ID, 'headline').text,
             'text': driver.find_element(By.CLASS_NAME, '_3RZvW').text
         }
        # driver.get('https://vp.rambler.ru/player/1.64.1/player.html#id=2061035&adTemplateId=0&playerTemplateId=11350&sspJparams=%7B%22puid6%22%3A%22RNEWS_ARMY%22%2C%22puid15%22%3A%22video%22%2C%22puid59%22%3A%22mobilization%3Amilitary%3Anegativity_weak%3Ahealth%3Adeath%3Abc%22%2C%22puid62%22%3A%221%22%7D&live=false&referrer=https%3A%2F%2Fnews.rambler.ru%2Farmy%2F49631828-chlen-sovfeda-pokazal-video-s-zhelayuschimi-krovi-vragov-mobilizovannymi%2F&aspectRatio=1.7777777777777777&widgetId=la15d0t9.s9_1')
        x = driver.find_element(By.CLASS_NAME, "_3RZvW").find_element(By.CLASS_NAME, "_1ODYE").find_element(By.TAG_NAME, "iframe").get_property("src")
        driver.get(x)

        last_new_view['video'] = driver.find_element(By.TAG_NAME, 'video').get_attribute('src')
        print(last_new_view)
        print(last_new_view['video'])
        if russian_links['rambler']['the_last_news'] == last_new_view['video']:
            pass
        else:
            index = last_new_view['text'].find('News.ru')
        await bot.send_document(chat_id=chennels_id['admin'],
                                document=image)
                                caption=f'<b>{last_new_view["title"]}</b>',
                                parse_mode='html')
            russian_links['rambler']['the_last_news'] = last_new_view['video']


async def news_by_belta():
    for news in russian_links['belta']:
        try:
            driver.get(russian_links['belta'][news]['link'])
            driver.find_element(By.CLASS_NAME, 'main_in_rubric').click()
            news = driver.find_element(By.CLASS_NAME, 'content_margin')
            last_new_views = {
                'image': news.find_element(By.TAG_NAME, 'img').get_attribute('src'),
                'title': news.find_element(By.TAG_NAME, 'h1').text,
                'text': ''
            }
            for i in news.find_element(By.CLASS_NAME, 'js-mediator-article').find_elements(By.TAG_NAME, 'p'):
                last_new_views['text'] = last_new_views['text'] + i.text
            if russian_links['belta'][news]['the_last_news'] == last_new_views['image']:
                pass
            else:
                x = 1024 - len(last_new_views["title"]) - 3
                success_send = await bot.send_photo(chat_id=chennels_id['admin'],
                                                    photo=last_new_views['image'],
                                                    caption=f'<b>{last_new_views["title"]}</b>\n \n{last_new_views["text"][:x]}',
                                                    parse_mode='html')
                success_send
                russian_links['belta'][news]['the_last_news'] = last_new_views['image']
                if len(last_new_views["text"][x:]) > 4096:
                    x_1 = 4096 - x
                    success_send_end = await bot.send_message(chat_id=chennels_id['admin'],
                                                              text=last_new_views["text"][x:x_1])
                else:
                    success_send_end = await bot.send_message(chat_id=chennels_id['admin'],
                                                              text=last_new_views["text"][x:])
                if len(last_new_views["title"]) + len(last_new_views["text"]) > 1024:
                    success_send
                    success_send_end
                    russian_links['moscowtimes'][news]['the_last_news'] = last_new_views['image']
                else:
                    await bot.send_photo(chat_id=chennels_id['admin'],
                                         photo=last_new_views['image'],
                                         caption=f'<b>{last_new_views["title"]}</b>\n \n{last_new_views["text"][:x]}',
                                         reply_markup=inline_kb,
                                         parse_mode='html')
                    russian_links['moscowtimes'][news]['the_last_news'] = last_new_views['image']
        except Exception as e:
            await send_error(f"""{russian_links['moscowtimes'][news]['link']} {e.args[0].replace(char, ' ')}""")


async def officelife():
    driver.get(russian_links['officelife']['link'])
    driver.find_element(By.CLASS_NAME, 'event-item').click()
    last_new_views = {
        'image': driver.find_element(By.CLASS_NAME, 'pic').find_element(By.TAG_NAME, 'img').get_attribute('src'),
        'title': driver.find_element(By.CLASS_NAME, 'article__title').find_element(By.TAG_NAME, 'h1').text,
        'text': driver.find_element(By.CLASS_NAME, 'article__content').text
    }
    if russian_links['officelife']['the_last_news'] == last_new_views['image']:
        pass
    else:
        if len(last_new_views['text']) > 1024:
            await bot.send_photo(chat_id=chennels_id['admin'],
                                 photo=last_new_views['image'],
                                 caption=f'<b>{last_new_views["title"]}</b>\n \n{last_new_views["text"][:1021]}',
                                 parse_mode='html')
        else:
            await bot.send_photo(chat_id=chennels_id['admin'],
                                 photo=last_new_views['image'],
                                 caption=f'<b>{last_new_views["title"]}</b>\n \n{last_new_views["text"]}',
                                 parse_mode='html')
        russian_links['officelife']['the_last_news'] = last_new_views['image']


async def euronews():
        driver.get('https://ru.euronews.com/news/international')
        driver.find_element(By.CLASS_NAME, 'o-block-topstories-newsy__articles').click()
        print('ok')
        last_new_views = {
            'image': driver.find_element(By.CLASS_NAME, 'pic').find_element(By.TAG_NAME, 'img').get_attribute(
                'src'),
            'title': driver.find_element(By.CLASS_NAME, 'c-article-title').find_element(By.TAG_NAME, 'h1').text,
            'text': driver.find_element(By.CLASS_NAME, 'c-article-content').text
        }
        if russian_links['belta'][news]['the_last_news'] == last_new_views['image']:

        if len(last_new_views['text']) > 1024:
            await bot.send_photo(chat_id=chennels_id['admin'],
                                 photo=last_new_views['image'],
                                 caption=f'<b>{last_new_views["title"]}</b>\n \n{last_new_views["text"][:1021]}',
                                 parse_mode='html')
        else:
            await bot.send_photo(chat_id=chennels_id['admin'],
                                 photo=last_new_views['image'],
                                 caption=f'<b>{last_new_views["title"]}</b>\n \n{last_new_views["text"]}',
                                 parse_mode='html')


@dp.callback_query_handler(lambda x: x.data == 'publish')
async def publish_in_chennel(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(chat_id=chennels_id['ru'],
                         photo=callback_query.message.photo[0]['file_id'],
                         caption=f"<b>{callback_query.message.caption.split(nl_char)[0]}</b>\n \n{callback_query.message.caption.split(nl_char)[1]}",
                         parse_mode='html')
    await bot.delete_message(callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)


@dp.callback_query_handler(lambda x: x.data == 'cancel')
async def cancel(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)


@dp.callback_query_handler(lambda x: x.data == 'change')
async def change_post(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(chat_id=chennels_id['ru'],
                         photo=callback_query.message.photo[0]['file_id'],
                         caption=f"<b>{callback_query.message.caption.split(nl_char)[0]}</b>\n \n{callback_query.message.caption.split(nl_char)[1]}",
                         parse_mode='html')
    await bot.delete_message(callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)


async def start_news_ru():
    aioschedule.every().hour.do(news_by_bbc_russian_big)
    aioschedule.every(10).minutes.do(news_by_moscowtimes_news_big_full)
    aioschedule.every(20).minutes.do(news_by_rambler)


    # ------------ tests --------------
    # aioschedule.every().minute.do(news_by_belta)
    # aioschedule.every().minute.do(officelife)
    # aioschedule.every().minute.do(euronews)


    # aioschedule.every().minute.do(news_by_bbc_russian_test)
    # aioschedule.every().minute.do(news_by_bbc_russian_big)
    # aioschedule.every().minute.do(news_by_rambler)
    # aioschedule.every().minute.do(news_by_moscowtimes_news_big_full)


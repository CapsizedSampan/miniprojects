import Request as keys
import logging
from telegram import *
from telegram.ext import *
import Responses as ans
import Qna as qna
from datetime import datetime

next = "\n\n Type 'next' to continue"
done = [False, 0, False, 0]
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

#stages
FIRST,SECOND, THIRD,FORTH  = range (4)
#callback data
ONE, TWO, THREE, FOUR, ALL = range(5)

print("Bot started...")

#start command
def start_command(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    update.message.reply_text("Type something to begin!")
    done[0] = False
    return FIRST

def impt_command(update,context):
    update.message.reply_text("EMERGENCY CONTACTS \nHuiru: @hui_ru \nMaple: ediblee")

def time_command(update,context):
    now = datetime.now()
    end = datetime.strptime("12/05/21, 17:30:00","%d/%m/%y, %H:%M:%S")
    diff = end - now
    exist = str(diff)
    final = exist.split(".")
    last = final[:-1]
    update.message.reply_text("Time left to 5.30pm: "+last[0])

def one_message(update, context):
    #update.message.reply_text('Where is location 1? HINT: 1,000 people were evacuated due to an incident. ')
    text = str(update.message.text).lower()
    s = "Where is location 1? HINT: 1,000 people were evacuated due to an incident. "
    #find corresponding ans to qn
    response = qna.one_response(text)
    if response == "Wrong! Please try again.":
        if done[0] == False:
            done[0] = True
            update.message.reply_text(s)
        else:
            update.message.reply_text(response + "\n" + s)
    elif response == 'Cannot restart lah just answer my qn!!':
        update.message.reply_text(response + "\n" + s)
    else:
        update.message.reply_text(response + next)
        return TWO

def two_message(update, context):
    text = str(update.message.text).lower()
    response = qna.two_response(text)
    s = "Where is location 2? HINT: Gong Cha was located here."

    if response == "Wrong! Please try again.":
        if done[1] == 0:
            done[1] = 1
            update.message.reply_text(s)
        elif done[1] < 6:
            update.message.reply_text(response + "\n\n" + s)
            done[1] = done[1] + 1
            print(done[1])
        else:
            update.message.reply_text(response + "\n"+ s + "\n[_ _ _ _ _ _ _ _  @  _ _ _ _ _ _]")

    else:
        update.message.reply_text(response + next)
        return THIRD

def three_message(update, context):
    text = str(update.message.text).lower()
    response = qna.three_response(text)
    s = "Where is location 3? HINT: Best Mala in NUS"

    if response == "Wrong! Please try again.":
        if done[2] == False:
            update.message.reply_text(s)
            done[2] = True
        else:
            update.message.reply_text(response + "\n" + s)

    else:
        update.message.reply_text(response + next)
        return FORTH

def four_message(update, context):
    text = str(update.message.text).lower()
    response = qna.four_response(text)
    s = "Where is location 4? \n HINT: Colourful roller chairs there!!"

    if response == "Wrong! Please try again.":
        if done[3] == 0:
            update.message.reply_text(s)
            done[3] = done[3] + 1
        elif done[3] < 6:
            update.message.reply_text(response + '\n'+ s)
            done[3] = done[3] + 1
        else:
            update.message.reply_text(response + '\n'+ s + "\n HINT: _ _ _ _   _ _ _")

    else:
        update.message.reply_text(response + "\n Please head to SDE2 ER1 for Station 3 :))")

def handle_message(update,context):
    text = str(update.message.text).lower()
    #find corresponding ans to qn
    response = ans.sample_response(text)

    update.message.reply_text(response)

def error(update,context):
    #print(f"Update{update} caused error {context.error}")
    update.message.reply_text("Sorry, I don't understand. Huh?")


def main():
     updater = Updater(keys.API_KEY, use_context = True)
     dp = updater.dispatcher
     j = updater.job_queue

#handlers for commands
     #dp.add_handler(CommandHandler("help", help_command))
     dp.add_handler(CommandHandler("time", time_command))
     dp.add_handler(CommandHandler("impt", impt_command))

#handler for quiz
     conv_handler = ConversationHandler(
         entry_points=[CommandHandler('start', start_command)],
         states={
             FIRST: [MessageHandler(Filters.text, one_message)],
             SECOND: [MessageHandler(Filters.text, two_message)],
             THIRD: [MessageHandler(Filters.text, three_message)],
             FORTH: [MessageHandler(Filters.text, four_message)],
         },
         fallbacks=[CommandHandler('start', start_command)],
     )
     dp.add_handler(conv_handler)

     dp.add_handler(MessageHandler(Filters.text, handle_message))
     dp.add_error_handler(error)
 #run_once(callback, when, context=None, name=None, job_kwargs=None)
#j.run_once(reminder,30)

#job_daily = j.reminder(daily_suggestion,  time=datetime.time(hour=10, minute=00, second=00))


# reminder for ppl to return
#def reminder(context: CallbackContext):
#    message = "Please start making your way back to Forum!"

 # send message to all users
#    id = r.get(keys).decode("UTF-8")
#    context.bot.send_message(chat_id=id, text=message)

#how long the bot takes to reply your message. 60 = checks every 60s. nothing = constantly checking
     updater.start_polling()
#makes sure the bot is alive when it isnt called
     updater.idle()



main()

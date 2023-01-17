from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import chatbot as chat


#   Example --------  bot_id = '1011350148:AAGg8tYwCimJrU9MUKK0ih_XJk901MqLbUQ'

bot_id = ''


updater = Updater(bot_id,use_context=True)

def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello sir, Welcome to the Bot.Please write\
		/help to see the commands available.")

'''def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/youtube - To get the youtube URL
	/linkedin - To get the LinkedIn profile URL
	/gmail - To get gmail URL
	/geeks - To get the GeeksforGeeks URL""")'''

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/pune_bus - To get the Pune Bus Details
	/state_bus - To get State Bus Timetable
	/google_maps - To open google maps""")


def puneBus_url(update: Update, context: CallbackContext):
	update.message.reply_text("Pune Bus URL = https://www.pcmcindia.gov.in/sutp/by pmpml.html")

def stateBus_url(update: Update, context: CallbackContext):
	update.message.reply_text("State Bus URL = https://msrtc.maharashtra.gov.in/index.php/bus timetable")

def googleMap_url(update: Update, context: CallbackContext):
	update.message.reply_text("Google Map URL = https://www.google.com/maps")


def gmail_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Your gmail link here (I am not\
		giving mine one for security reasons)")


def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube Link =>\
	https://www.youtube.com/")


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"LinkedIn URL => \
		https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")


def geeks_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"GeeksforGeeks URL => https://www.geeksforgeeks.org/")


def unknown(update: Update, context: CallbackContext):
	print(update.message.text)
	update.message.reply_text(chat.chatbot(update.message.text.lower()))
		#"Sorry '%s' is not a valid command" % update.message.text )


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(CommandHandler('pune_bus', puneBus_url))
updater.dispatcher.add_handler(CommandHandler('state_bus', stateBus_url))
updater.dispatcher.add_handler(CommandHandler('google_maps', googleMap_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
#updater.dispatcher.add_handler(MessageHandler(
#	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

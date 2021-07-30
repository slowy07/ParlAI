#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# Possible roles of an agent during task
NO_ROLE = 0
WIZARD = 1
APPRENTICE = 2
IN_TRAINING = 10
WIZARD_IN_TRAINING = WIZARD + IN_TRAINING
APPRENTICE_IN_TRAINING = APPRENTICE + IN_TRAINING
# The role_id to role_name mapping
ROLE_NAMES = {WIZARD: 'Wizard', APPRENTICE: 'Apprentice'}

# The keys to get agent qualification data from opt.
SAVED_DATA_WORKER_KEY = 'worker'
SAVED_DATA_IS_WIZARD_KEY = 'is_wizard'
SAVED_DATA_ROLE_QUALIFICATION_DATA_KEY = 'qualification_dict'
ROLE_QUALIFICATION_NAME_KEY = 'role_qname'

# OnBoardingSteps
# Make sure these number are consistent with OnboardingSteps,
# as they are defined in the SidePane.jsx frontend file.
# TODO: combine the definitions into one source of truth.
ONBOARDING_STEPS = {
    'NOT_ONBOARDING': 0,
    'CHAT_INTERFACE': 1,
    'TRY_SEARCH': 2,
    'PERSONA_WIZARD': 3,
    'PERSONA_APPRENTICE': 4,
    'WAITING': 10,
}

# Name of (bot)agents involved in the task world
ONBOARDING_AGENT = 'OnboardingBot'
PERSONA_AGENT = 'PersonaAgent'
SEARCH_AGENT = 'SearchAgent'
COORDINATOR_AGENT = 'Coordinator'


# The wait time in seconds to allow the agents read the instructions during the onboarding.
# After this, we allow them to continue after a small action (for example, type anything).
# The keys are the onboarding tutorial step; values are the wait times corresponding to that.
TUTORIAL_WAIT_TIMES = {'chat-interface': 1, 'persona': 2, 'knowledge': 2}

# Constants for checking onboarding work quality
WORKER_REJECT_REASON = 'reason_to_reject'
MIN_AVG_CHAR_LENGTH_UTTERANCES = 10
MIN_AVG_WORD_LENGTH_UTTERANCES = 5
MIN_NUM_SEARCH_ONBOARDING = 2
MIN_NUM_SELECTED_SENTENCES_ONBOARDING = 2

# Long messages
ONBOARDING_WELCOME = (
    'Welcome onboard!\n'
    'Here you will have an engaging, '
    'knowledgeable chat with another person. '
    'This is the chat interface you will be using.\n'
    'Our interactive tutorial introduces you to the main task. '
    'If you finish all the steps successfully, '
    'and in reasonable time, we redirect you to the main task.\n'
    'Please have a friendly chitchat pretending you live in a '
    'world unaffected by covid and recent controversial events.'
)

ONBOARDING_ACKNOWLEDGE_UNDERSTOOD = (
    'Please acknowledge that this is clear '
    'in your response message '
    '(for example, type \'I understand.\' in response.)'
)

FINISHED_ONBOARDING = (
    'Good job, you now know how this task works!\n'
    'You can check the task instructions on the left at any time '
    'during the task. Please wait while we pair '
    'you with another participant.'
)

WIZARD_INTRODUCE_KNOWLEDGE = (
    'During this chat you must pretend that you are a knowledgeable '
    'entity with conversational ability rather than a human being '
    '(imagine a digital friend on a smartphone).'
    'So you can talk about the world, but your character is NOT able to '
    'engage in physical activities such as sport activities or eating.'
)

WIZARD_INTRODUCE_SEARCH = (
    'We will provide a search bar for you '
    'to look up useful knowledge about topics that interest '
    'your chat partner during the conversation.\n'
    'You may try search as many times as you may like '
    'to find useful information that helps you craft '
    'engaging and informative messages.\n'
    'Please conduct a natural conversation and avoid copy/paste.'
)

WIZARD_TRY_SEARCH = (
    'See the blinking area (in the left panel) '
    'for the search bar you will be using during this task. '
    'During the task, when you use this search bar, '
    'it will bring up a number of articles from the internet. '
    'You can click on an article to show '
    'it\'s content, that is split into sentences. '
    'Use information from these sentences '
    'to have an informed conversation.\n\n'
    'When you use knowledge from one or more sentences, '
    'please select them (click the checkbox next to those '
    'sentences) before sending your message.\n'
    'If you do not use any knowledge from search results, '
    'select the checkbox for '
    '"Did not use search results for this message."\n\n'
    'Now try out the search functionality to '
    'craft a message with information on a topic of your choise '
    '(Yoga, sushi, Star wars, anything you choose). '
    'Here are the steps :\n'
    '  1- use the bar to search.\n'
    '  2- check the search results for finding useful information.\n'
    '  3- write your message using knowledge you find in the search results.\n'
    '  4- make sure you select the checkmark for sentences you used.\n'
    '  5- send the message.'
)

WIZARD_INTRODUCE_APPRENTICE_PERSONA = (
    'You can see your partner\'s assigned persona '
    'description in the left pane (see the blinking box). '
    'The purpose of the task is to have an in-depth conversation '
    'with your chat partner about THEIR assigned interests.\n'
    'It is very important to keep in mind that this is a chitchat: '
    'unless it is necessary, do NOT bring up random facts in the middle of conversation. '
    'For example, if your chat partner likes a music band '
    'do not keep talking about band members names or birthdays.\n\n'
    'Use your search bar on the left and craft a message '
    'that interests your partner, based on their persona, '
    'using information you find on internet.\n'
    'Don\'t forget to select the sentences from the '
    'search results that helped you craft that message.'
)

APPRENTICE_INTRODUCE_PERSONA = (
    'At the beginning of this task we will ask you to '
    'choose a persona for yourself. '
    'We keep your selected persona in the left pane '
    '(See the example persona inside the blinking box).\n'
    'During this chat you play the role of someone with that persona. '
    'The purpose of the task is to have '
    'an in-depth conversation with your chat partner '
    'about the interests of someone with your assigned persona.'
)

APPRENTICE_INTRODUCE_WIZARD = (
    'Imagine your chat partner is a non-human entity '
    'you can chat to, for example a digital friend living inside '
    'your phone. So you can ask their opinion about the world, '
    'but they are not able to do physical activities, '
    'such as playing basketball or eating. Don\'t forget that '
    'the conversation should focus on the interests '
    'of the persona that you play during this task.'
)

APPRENTICE_INTRODUCE_WIZARD_KNOWLEDGE = (
    'Your chat partner has extensive knowledge '
    'about many things, and access to lots of information.\n'
    'Your partner will strive to enlighten you '
    'about your topics of interest, according to your persona. '
    'Feel free to dive deep discussing these topics.'
)

APPRENTICE_PERSONA_ROLE_INSTRUCTION = (
    'Let\'s assume you are in the main task and you '
    'have the example persona that we show now '
    '(blue box on the left). '
    'Please say something interesting about '
    'your role\'s persona to continue. '
    'Don\'t forget to assume the role of someone with '
    'that persona for the rest of this task.'
)

APPRENTICE_CHITCHAT_INSTRUCTION = (
    'Imagine you are in the main chat. Go ahead and send them a '
    'chitchat message, assuming your assigned persona.'
)

APPRENTICE_PERSONA_MSG_INSTRUCTION = (
    'Go ahead and try writing a message '
    'about your example role\'s persona to your partner. '
    'You may even ask them questions if you want.'
)

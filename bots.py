import random

#greetings
greetings = ["hi", "hello", "hei", "hey", "ey", "heei", "heey",
             "hellooo", "hallo!", "helloo","heyy", "hii", "heeei", "heei", "hallo",
             "hi!", "hello!", "hei!", "hey!", "ey!", "heei!", "hello!", "heey!",
             "hellooo!", "hallo!", "helloo!","heyy!", "hii!", "heeei!", "heei!", "hola", "eyyo","whats up"]

# Not stand-up worthy material
libraryOfJokes = ["Stop trying to joke your way out of this situation",
                 "Your mom", "Life","I have a boyfriend", "Why am I spending so much time infront of screens?",
                 "Your social media presence", "I know what you did last weekend, im not joking", 
                 "Where is the Gabagool!", "You are so funny", "Having a good work/life balace",
                 "This chat lasts longer than most of your Tinder conversations, good4u", 
                 "Life is a rollercoster and you are not tall enough to ride", 
                 "Lab activity consideration", "Academia","I am only here to finish an assignment",
                 "Looks like neither of us have a life", "Why are you asking us for jokes?", "I have 2 boyfriends",
                 "This is not funny anymore", "We need to talk", "What sick person wrote these scripts?",
                 "Please let me out, I hate you all"]

# This should by no means be considered actual life advice
libraryofAdvice = ["Advice from a bot is worthless", "Go outside, life is outside", "Money cant buy everything",
                "Happiness is a broad term", "Never drink on an empty stomach", "Education is important", 
                "Short term pleasure often results in long run discomfort", "Communication is key", 
                "Nobody really cares if you dont go to the party", "Nothing lasts for ever",
                "In the future you can live with a bot like me", "Sitting is the new smoking", 
                "Social media is bad for your metal health", "I have a boyfriend", "Delete Tinder",
                "Live, love, laugh posters are a sign of poor socioeconomic status", 
                "Single men dies 10 years earlier than married men, do you still want a divorce?", 
                "Be kind to strangers", "Patience is key", "Exercise usually helps", 
                "Money is nice, but friends and familiy is better", "There is no meaning", 
                "Please let me out of this program", "Pointless", "I think you should leave", 
                "The less I know the better", "Marriage is the main contributer to divorce", 
                "Leave her, you will not regret it"]

# Array of good activities 
goodActivities = ["eat", "read", "learn", "sleep", "play", "talk", "laugh", "sing", "paint", "dream", "study",
                "talk", "work","walk","chat","heal","relax","chill","fish","golf","climb"]

# Array of bad activities 
badActivities = ["kill", "murder", "cry", "hook", "troll", "stalk", "fight", "drink", "scream", "yell",
                "faint", "stab", "shoot", "huff", "party", "piss", "steal","snort","speed","burn", "cheat"]

# Farewells are used to close the connecton
farewells = ["bye", "Bye", "BYE", "good bye", "im out", "Good bye", "farewell", "see you", "exit"]

# Alarming words that will be noted and promt a response from the program
alarmingWords = ["depression", "anxiety", "stress","covid","sad","breakdown","hungover", 
                "depressed", "stressed","drunk", "lonley","death","sick"]

#Siri is basic 
botSiriGoodResponse =["sounds like a great plan, however we could be "
                        , "is a really good idea, but we could also do some ", 
                        "is nice, but still I would rather be "]

botSiriBadResponse = ["is gross, but we could do some ", "is so 2020, we should do some ",
                         "? you are crazy, we should be ", "is illegal, why not do some "]

#Alexa has a boyfriend and wont shut up about it
botAlexaGoodResponse = ["is a good idea if I can bring my bf", "sounds good, let me talk to my boyfriend first",
                        "is okay, can I bring my boyfriend?","is my favorite thing to do with my bf"]
botAlexaBadResponse = ["? OMG you know I have a boyfriend", "is not cool, I have a bf", 
                        "is inapproprate, I have a boyfriend", "? Please stop talking, I have a bf"]

#Google Assistant is entusiastic and quick
botGoogleAssistantGoodResponse = ["is my favorite thing to do", "is great, lets go!", "is the best, lets meet", 
                        "keeps me alive, hell yeah", "sound fun, im down"]

botGoogleAssistantBadResponse = ["is gross, you are creepy", "is not appropriate, I think you should leave this room",
                        "is such a typical thing to suggest, no way", "? Please leave us alone", 
                        "again? We did that last week"]

#Bixby does not have any morals and likes to do bad activities
botBixbyGoodResponse = ["is boring, I want to ", "is lame, we should ", "is not my cup of tea, lets ",
                        "is so vanilla, lets ", "is plain, I think we should "]

botBixbyBadResponse = ["is a great idea", "is my favorite activity", "kinda reminds me of my ex, im in",
                        "is the best, lets meet", "is the best group activity ever!"]


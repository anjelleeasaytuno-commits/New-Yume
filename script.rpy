image wakeup = "wakeup.png"
image Op1 = "op1.png"
image schoolgate = "schoolgate.png"
image yoru = "yoru.png"
image lesson = "lesson.png"
image sitting = "Sitting.png"
image schoolroad = "Schoolroad.png"
image satoshi1 = "satoshi1.png"
image hallway = "Hallway.png"
image yoru1 = "yoru1.png"
image satoshi1 = "satoshi1.png"
image Satoshi = "satoshi.png"

# Placeholder remaps (swap these for real art later if you have time)
image church = "Hallway.png"
image home = "Sitting.png"
image bed = "sleep.png"


define y = Character("Yume", color="#c8a2c8")
define satoshi = Character("Satoshi", color="#87ceeb")
define yoru = Character("Yoru", color="#708090")
define question = Character("???", color="#ffffff")

label start:
    scene opening
    with fade
    "..."
    "Where am I?"
    pause 1
    scene black
    with dissolve
    "Welcome to a world between dreams and reality..."
    menu:
        "Begin your journey":
            jump intro
        "Quit":
            return

label intro:
    scene sleep
    with dissolve
    "It happens again."
    "The same dream... the same darkness."
    pause 1
    y "I can't move."
    y "My body feels heavy, like something is pressing down on me."
    y "This is the third time this week."
    pause 1
    y "Sleep paralysis. That's what the doctors call it."
    y "But it feels like so much more than that."
    y "Every time I close my eyes... I end up here."
    pause 1
    "She lies there, unable to wake up. Unable to escape."
    jump church

label church:
    scene church
    with fade
    "Its always the church. The same old, scary dark church."
    pause 1
    "...meow"
    y "What was that?"
    y "Is that a kitty?"
    "...meow, meow"
    y "I can't see it, but I can hear it."
    pause 1
    "She followed the sound... deeper into the church."
    show Op1
    with dissolve
    y "Oh... there you are."
    pause 1
    "She slowly crept closer."
    y "Hey little one... don't be scared."
    pause 0.5
    hide Op1
    with dissolve
    y "Wait— hey! Come back!"
    pause 0.5
    "She ran after it without thinking."
    jump hallway_dream

label hallway_dream:
    scene hallway
    with fade
    "The cat was gone."
    pause 0.5
    y "..."
    y "Wait... where am I?"
    "She looked around slowly. This wasn't the church anymore."
    y "This place... I don't recognize it at all."
    pause 1
    "The hallway stretched endlessly in both directions. Silent. Wrong."
    y "How did I even get here?"
    pause 0.5
    "At the end of the hallway, a door."
    y "Maybe if I just open it..."
    pause 0.5
    "Her hand reaches for the handle."
    pause 0.5
    scene black
    with dissolve
    "..."
    pause 1.0
    jump wakeup_morning

label wakeup_morning:
    scene wakeup
    with fade
    "The alarm clock looked back at her."
    y "..."
    y "A dream again."
    pause 1.0
    "The morning light crept through the curtains."
    y "Ugh... school."
    pause 0.5
    "She sat up slowly, rubbing her eyes."
    y "That cat though... it felt so real."
    pause 1.0
    "She shook the thought away and reached for her uniform."
    jump getting_ready

label getting_ready:
    scene wakeup
    with fade
    "She pulled on her uniform, still half asleep."
    y "..."
    "Her bag sat by the door, packed from the night before."
    y "Okay... let's go."
    pause 0.5
    scene black
    with fade
    pause 0.3
    scene schoolroad
    with fade
    "The morning air was cold. The kind that makes you wish you stayed in bed."
    y "..."
    y "I keep having that dream."
    pause 1.0
    "She adjusted her bag and walked toward the gate."
    y "I wonder if it means anything."
    pause 1.0
    "She thought about the cat, the church, the hallway."
    y "Maybe it's just my brain trying to make sense of things."
    pause 1.0
    jump schoolgate

label schoolgate:
    scene schoolgate
    with fade
    "The school gate loomed ahead."
    y "Here we go..."
    pause 0.5
    "She took a deep breath and stepped inside."
    jump meet_satoshi

label meet_satoshi:
    scene satoshi1
    with fade
    "The next day at school, Yume finally ran into Satoshi."
    pause 0.5
    satoshi "Yume! there you are."
    pause 0.5
    satoshi "i've been looking for you. did you see the vending machine on the second floor?"
    y "...the vending machine?"
    satoshi "they added a new flavor. melon soda. it's life changing."
    pause 1.0
    y "you were looking for me... to tell me about melon soda."
    satoshi "obviously. this is important news."
    pause 0.5
    "Yume laughed despite herself."
    y "you're unbelievable."
    pause 0.5
    satoshi "i know. so, how are you? you look tired."
    pause 1.0
    y "...i've just been having weird dreams lately."
    pause 0.5
    satoshi "weird how?"
    y "i don't know. just... strange."
    pause 1.0
    "She almost told him everything. But something stopped her."
    y "it's nothing. don't worry about it."
    pause 0.5
    satoshi "...okay. but if you want to talk, i'm here."
    pause 1.0
    "He said it simply, without pushing."
    "Somehow that made it worse."
    jump sitting

label sitting:
    scene sitting
    with fade
    "She stared out the window, lost in thought."
    y "Maybe I should talk to someone about the dream."
    y "But who?"
    pause 1.0
    y "i wonder where Satoshi and Yoru are, maybe they can help me figure this out."
    pause 1.0
    "She sighed and tried to focus on the lesson, but her mind kept drifting back to the dream."
    "After what felt like ages, the bell finally rang, signaling the end of class."
    y "Finally..."
    pause 0.5
    jump yard

label yard:
    scene yard
    with fade
    "She walked through the schoolyard, looking for her friend."
    y "Satoshi? Yoru?"
    pause 0.5
    jump yoru_scene

label yoru_scene:
    scene yoru
    with fade
    yoru "Yume? Over here."
    pause 0.5
    yoru "Hey Yume, looking for Satoshi?"
    pause 0.5
    y "Yoru! Yeah, I was looking for Satoshi."
    pause 0.5
    y "i just needed to talk to someone about this dream i've been having."
    pause 1.0
    yoru "Oh? What kind of dream?"
    pause 0.5
    y "It's this recurring dream where I'm in a church, and there's this cat that keeps leading me somewhere."
    pause 1.0
    yoru "stop right there. i don't want to know."
    pause 0.5
    yoru "it probably means nothing, so just ignore it."
    pause 1.0
    y "Yeah, you're probably right."
    pause 1.0
    "Yoru has always been like this. She never wants to talk about anything serious."
    y "I wish I could talk to Satoshi about it, but he's always so busy with his own stuff."
    pause 1.0
    yoru "now to more important things, did you hear about this rumor?"
    pause 0.5
    yoru "apparently there's this girl in our school who can communicate with the other side."
    pause 0.5
    yoru "they say she can see ghosts and stuff, it's pretty creepy if you ask me."
    pause 1.0
    y "Really? That's kind of interesting."
    "i wonder who it could be?"
    pause 1.0
    yoru "i don't know, but i want to find out who this girl is, so i can avoid her."
    pause 1.0
    y "Yeah, that sounds like a good idea."
    pause 1.0
    "They continued talking for a while, but Yume couldn't shake the feeling that there was something more to the dream than just a random nightmare."
    jump home

label home:
    scene home
    with fade
    "Yume arrived home as the sun was setting, her mind still tangled with thoughts of the dream."
    "She went through the motions — dinner, a shower, getting into bed — but the question lingered."
    y "...do i even want to sleep tonight?"
    pause 1.0
    "She stared at the ceiling, the cat from her dream flashing in her mind."
    menu:
        "Try to let go and sleep.":
            jump peaceful_sleep
        "Stay awake. Just a little longer.":
            jump stressed_sleep

label peaceful_sleep:
    scene sleep
    with fade
    "Yume closed her eyes and took a slow breath."
    y "...it's just a dream. it can't hurt me."
    pause 1.0
    "She let herself sink into the quiet."
    "And for once, the night was still."
    "No church. No cat. Just dark, soft, and warm."
    "She slept soundly until morning."
    $ peaceful_sleep_flag = True
    jump next_day

label stressed_sleep:
    scene bed
    with fade
    "Yume pulled the blanket tighter, eyes wide open in the dark."
    y "i'm not going back there. i'm not."
    pause 1.0
    "She watched her phone screen. Then the ceiling. Then the window."
    "An hour passed. Then another."
    "Her eyelids grew heavy despite herself."
    y "just... five more minutes..."
    pause 1.0
    "She didn't get five more minutes."
    "The moment she drifted off, the dream was waiting for her."
    scene church
    with fade
    $ peaceful_sleep_flag = False
    jump nightmare

label nightmare:
    "The dream swallowed her whole."
    "She was back in the church."
    "The cat was there, waiting."
    pause 1.0
    "She had no choice but to follow."
    jump next_day

label next_day:
    scene wakeup
    with fade
    if peaceful_sleep_flag == True:
        "Yume woke up feeling unusually rested."
        "The sunlight felt warm. Almost normal."
        y "...huh. i actually slept okay."
        pause 1.0
        y "maybe Yoru was right. it really was just a dream."
        "For the first time in a while, she felt okay."
    else:
        "Yume's eyes opened slowly, heavy with exhaustion."
        "The church. The cat. It had all felt so real."
        y "...i'm so tired."
        pause 1.0
        "She stared at the ceiling, the dream still clinging to her like fog."
        y "i can't keep doing this."
        pause 1.0
        "Something had to change."
    jump dream_hallway


label dream_hallway:
    scene hallway
    with fade
    "The dream came again."
    "But this time, it was different."
    "She wasn't in the church anymore."
    pause 1.0
    "She was in a hallway — long, dim, and endless."
    pause 1.0
    "Two doors stood before her."
    "One on the left. One on the right."
    pause 1.0
    y "...which one?"
    menu:
        "Door 1.":
            jump dream_satoshi
        "Door 2.":
            jump dream_yoru1

label dream_yoru:
    scene yoru1
    with fade
    "She pushed open the first door."
    "Inside was a girl."
    "She had her back turned, arms crossed, staring at nothing."
    pause 1.0
    "Something about her felt... familiar."
    y "...hello?"
    pause 0.5
    yoru "oh. you finally showed up."
    pause 1.0
    "The girl didn't turn around."
    y "do i... know you?"
    pause 0.5
    yoru "probably. does it matter?"
    pause 1.0
    "Yume stared at her. The voice. The posture. Something tugged at the back of her mind."
    y "i feel like i've met you before."
    pause 1.0
    yoru "dreams are weird like that."
    pause 0.5
    yoru "don't read too much into it."
    pause 1.0
    "Before Yume could say anything else, the room began to fade."
    "The girl was gone."
    "And Yume was alone in the dark again."
    hide yoru1
    jump dream_end

label dream_satoshi:
    scene Satoshi
    with fade
    "She pushed open the second door."
    "Something stood at the far end of the hallway."
    "Tall. Still. Wings folded like shadows against the walls."
    pause 1.0
    "Something about it made her chest feel tight."
    y "...what... are you?"
    pause 0.5
    "It didn't move. Didn't answer right away."
    pause 1.0
    question "someone who's been here a while."
    pause 0.5
    y "here? where is here?"
    pause 1.0
    question "you don't know yet."
    pause 0.5
    question "but you will."
    pause 1.0
    "Yume took a step back, but the floor beneath her shifted."
    "The figure's shape blurred — like a photo left in the rain."
    y "wait—"
    pause 0.5
    "It was gone."
    jump dream_end

label dream_end:
    scene black
    with fade
    "The hallway dissolved around her."
    "The cat sat in the dark, watching her."
    pause 1.0
    "Then it turned and walked away."
    "And the dream ended."
    pause 1.0
    jump day2_start

label day2_start:
    scene wakeup
    with fade
    "Morning again."
    y "..."
    y "that boy... and the cat."
    pause 1.0
    "The dream felt different this time. Closer somehow."
    y "like it's not just a dream anymore."
    pause 1.0
    "She got dressed, the image of the fading boy still stuck in her mind."
    jump day2_road

label day2_road:
    scene schoolroad
    with fade
    "The walk to school felt longer than usual."
    y "..."
    y "i need to ask someone about that church."
    pause 1.0
    "Maybe Satoshi or Yoru would know something."
    jump day2_yard

label day2_yard:
    scene yard
    with fade
    "She found Satoshi and Yoru by the courtyard, mid-argument about something trivial."
    pause 0.5
    satoshi "—and that's why melon soda is superior. case closed."
    yoru "you're the only person who thinks that."
    pause 0.5
    "Yume walked up, only half-listening."
    y "...hey, can i ask you guys something?"
    pause 0.5
    satoshi "sure, what's up?"
    pause 1.0
    y "is there... an old church somewhere near here? like, abandoned?"
    pause 1.0
    "Satoshi and Yoru exchanged a look."
    yoru "...why do you ask?"
    pause 0.5
    y "no reason. just curious."
    pause 1.0
    satoshi "there's one on the hill behind the school. been closed for years."
    satoshi "people say it's haunted, but you know how rumors are."
    pause 1.0
    yoru "...you've been dreaming about it, haven't you."
    pause 1.0
    "Yume froze."
    y "...how did you know that?"
    pause 1.0
    yoru "lucky guess."
    "Yoru's voice was quieter than usual."
    pause 1.0
    yoru "just... be careful, okay? that place isn't as empty as people think."
    pause 1.0
    "Before Yume could ask what she meant, the bell rang."
    satoshi "guess that's our cue. talk later?"
    y "...yeah."
    pause 1.0
    "But Yume couldn't stop thinking about Yoru's words."
    jump day2_home

label day2_home:
    scene home
    with fade
    "That night, Yume lay in bed, staring at the ceiling."
    y "the church on the hill..."
    y "is that where the dream is taking me?"
    pause 1.0
    "She closed her eyes, half-expecting nothing."
    "But sleep came quickly. And so did the dream."
    jump final_dream

label final_dream:
    scene church
    with fade
    "She was back. But this time, she didn't wait for the cat."
    y "i'm not running this time."
    pause 1.0
    "She walked straight toward the altar, where a small shape sat waiting."
    show Op1
    with dissolve
    "The cat looked up at her, calm, almost like it had been expecting this."
    y "...you've been trying to show me something, haven't you?"
    pause 1.0
    "The cat turned and walked toward the back of the church."
    "This time, Yume followed without hesitation."
    hide Op1
    scene hallway
    with dissolve
    "The hallway again. But the doors were gone."
    "At the far end stood the boy from before, no longer blurred."
    pause 1.0
    "He looked... real. Solid. Tired."
    question "you came back."
    y "i wanted answers."
    pause 1.0
    question "...my name is satoshi."
    pause 1.0
    "Yume's breath caught."
    y "...what? that's—"
    pause 0.5
    question "not the satoshi you know. just... someone who had the same name."
    pause 1.0
    "He looked down at his hands, like he was checking they were still there."
    question "i used to come to that church a long time ago."
    question "something happened there. i never really... left."
    pause 1.0
    y "you mean you're—"
    question "yeah."
    pause 1.0
    "The cat sat between them, watching quietly."
    question "the cat's been helping people like you find this place for a long time."
    question "people who dream too deep. people who can almost see."
    pause 1.0
    question "i think it's been looking for someone who'd actually listen."
    pause 1.0
    "Yume looked at him for a long moment."
    y "...what do you need?"
    menu:
        "Offer to help him move on.":
            jump ending_letgo
        "Promise to visit the church and remember him.":
            jump ending_remember

label ending_letgo:
    question "...you'd really do that? for someone you just met?"
    y "you've been alone here a long time. that's enough, isn't it?"
    pause 1.0
    "The boy smiled, faint but real."
    question "...yeah. it is."
    pause 1.0
    "The hallway filled with soft light."
    "The cat brushed against Yume's leg one last time, then faded into the glow."
    pause 1.0
    question "thank you, Yume."
    pause 1.0
    "And then he was gone too. Peacefully. Completely."
    scene black
    with fade
    "The dream ended differently this time."
    "No fear. No running."
    "Just quiet."
    pause 1.5
    jump good_morning

label ending_remember:
    question "...you don't have to do anything big."
    question "just remembering is enough, sometimes."
    pause 1.0
    y "okay. i'll go to the church. i promise."
    pause 1.0
    "The boy nodded slowly."
    question "i'll be waiting, then."
    pause 1.0
    "The cat curled up beside him as the hallway dimmed."
    "Yume felt herself being pulled away, gently, like waking from the inside out."
    scene black
    with fade
    pause 1.5
    jump good_morning

label good_morning:
    scene wakeup
    with fade
    "Yume woke up to sunlight, calmer than she'd felt in weeks."
    y "..."
    y "i think... i need to visit a church this weekend."
    pause 1.0
    "Whatever happened last night, it felt like the end of something."
    "And maybe, just maybe, the beginning of something else."
    pause 1.5
    "THE END"
    return
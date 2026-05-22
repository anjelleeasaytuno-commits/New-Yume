image wakeup = "wakeup.png"
image Op1 = "Op1.png"
image schoolgate = "schoolgate.png"
image yoru = "yoru.png"
define y = Character("Yume", color="#c8a2c8")
define s = Character("Satoshi", color="#87ceeb")
define yoru = Character("Yoru", color="#708090")

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
    "Its always the church. The same old, scary dark church."
    pause 1
    "...meow"
    y "What was that?"
    y "Is that a kitty?"
    "...meow, meow"
    y "I can't see it, but I can hear it."
    pause 1
    "She followed the sound... deeper into the church."

    scene church
    with fade
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

    # Dream starts breaking
    "Her hand reaches for the handle."
    pause 0.5
    scene black
    with dissolve
    "..."
    pause 1.0

    # Wake up
    scene wakeup
    with fade
    "The alarm clocked looked back at her."
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

label schoolgate:
    scene schoolgate
    with fade
    "The school gate loomed ahead."
    y "Here we go..."
    pause 0.5
    "She took a deep breath and stepped inside."

label classroom:
    scene classroom
    with fade
    "The classroom was bustling with students."
    y "god i hate this place"
    pause 1.0
    "She found her seat and sat down, trying to ignore the noise around her."
    y "I hope no one talks to me today."
    pause 1.0

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
    "after what felt like ages, the bell finally rang, signaling the end of class."
    y "Finally..."
    pause 0.5

label yard:
    scene yard
    with fade
    "She walked through the schoolyard, looking for her friend."
    y "Satoshi? Yoru?"
    pause 0.5
    with dissolve

    label yoru:
        scene yoru
        with fade
    yoru "Yume? Over here."
    pause 0.5
    yoru "Hey Yume looking for Satoshi?"
    pause 0.5
    y "Yoru! Yeah, I was looking for Satoshi."
    pause 0.5
    y "i just needed to talk to someone about this dream i've been having."
    pause 1.0
    yoru "Oh? What kind of dream?"
    pause 0.5
    y "It's this recurring dream where I'm in a church, and there's this cat that keeps leading me somewhere."
    pause 1.0
    yoru "stop right there. i dont want to know." 
    pause 0.5
    yoru " it probably means nothing, so just ignore it."
    pause 1.0
    y "Yeah, you're probably right."
    pause 1.0
    "yoru has always been like this, she never wants to talk about anything serious."
    y "I wish I could talk to Satoshi about it, but he's always so busy with his own stuff."
    pause 1.0
    yoru "now to more important things, did you hear about this rumor?"
    pause 0.5
    yoru "apparently there's this girl in our school who can communicate with the other side."
    pause 0.5
    yoru "they say she can see ghosts and stuff, it's pretty creepy if you ask me."
    pause 1.0
    y "Really? That's kind of interesting."
    "i wonder who can it be?"
    pause 1.0
    yoru "i dont know, but i want to find out who this girl is, so i can avoid her."
    pause 1.0
    y "Yeah, that sounds like a good idea."
    pause 1.0
    "They continued talking for a while, but Yume couldn't shake the feeling that there was something more to the dream than just a random nightmare."


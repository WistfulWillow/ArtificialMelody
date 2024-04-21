# show alina mouth_neutral_talk
# -milituni_coat -milituni_main workuni_main workuni_waistcoat workuni_blazer
# -hair_1 hair2_back hair_2_1

define l = Character("Alina",image="alina")

layeredimage alina:
    attribute hair2_back:
        "images/chrs/alina/layered_assets/hair/hair_2_2.png"

    group base:
        attribute base default:
            "images/chrs/alina/layered_assets/base/base.png"
        attribute base_o4:
            "images/chrs/alina/layered_assets/base/base_outfit4.png"
    
    attribute blush:
        "images/chrs/alina/layered_assets/base/blush.png"
    
    group eyebrows:
        attribute eyebrow_angry:
            "images/chrs/alina/layered_assets/expressions/separate/eyebrows/angry.png"
        attribute eyebrow_happy:
            "images/chrs/alina/layered_assets/expressions/separate/eyebrows/happy.png"
        attribute eyebrow_neutral default:
            "images/chrs/alina/layered_assets/expressions/separate/eyebrows/neutral.png"
        attribute eyebrow_sad:
            "images/chrs/alina/layered_assets/expressions/separate/eyebrows/sad.png"
    
    group eyes:
        attribute eye_open:
            "images/chrs/alina/layered_assets/expressions/separate/eyes/open.png"
        attribute eye_closed:
            "images/chrs/alina/layered_assets/expressions/separate/eyes/closed.png"
        attribute eye_blink default:
            "alina_blink"
    
    group mouth:
        attribute mouth_angry:
            "images/chrs/alina/layered_assets/expressions/separate/mouth/angry.png"
        attribute mouth_angry_talk:
            "images/chrs/alina/layered_assets/expressions/separate/mouth/angry_talk.png"
        attribute mouth_happy:
            "images/chrs/alina/layered_assets/expressions/separate/mouth/happy.png"
        attribute mouth_happy_talk:
            "images/chrs/alina/layered_assets/expressions/separate/mouth/happy_talk.png"
        attribute mouth_neutral default:
            "images/chrs/alina/layered_assets/expressions/separate/mouth/neutral.png"
        attribute mouth_neutral_talk:
            "images/chrs/alina/layered_assets/expressions/separate/mouth/neutral_talk.png"
        attribute mouth_sad:
            "images/chrs/alina/layered_assets/expressions/separate/mouth/sad.png"
        attribute mouth_sad_talk:
            "images/chrs/alina/layered_assets/expressions/separate/mouth/sad_talk.png"
    
    attribute milituni_main default:
        "images/chrs/alina/layered_assets/clothes/military_uni/main.png"
    group milicoat:
        attribute milituni_coat default:
            "images/chrs/alina/layered_assets/clothes/military_uni/coat.png"
        attribute milituni_coat_off null
    
    attribute workuni_main:
        "images/chrs/alina/layered_assets/clothes/work_uni/main.png"
    attribute workuni_waistcoat:
        "images/chrs/alina/layered_assets/clothes/work_uni/waistcoat.png"
    attribute workuni_blazer:
        "images/chrs/alina/layered_assets/clothes/work_uni/blazer.png"
    
    attribute casualwarm_main:
        "images/chrs/alina/layered_assets/clothes/casual_warm/main.png"
    
    attribute casualcold_main:
        "images/chrs/alina/layered_assets/clothes/casual_cold/main.png"
    
    group hair_mains:
        attribute hair_1 default:
            "images/chrs/alina/layered_assets/hair/hair_1.png"
        attribute hair_2_1:
            "images/chrs/alina/layered_assets/hair/hair_2_1.png"
    
    group bows:
        attribute bow_black default:
            "images/chrs/alina/layered_assets/clothes/bows/bbow.png"
        attribute bow_red:
            "images/chrs/alina/layered_assets/clothes/bows/rbow.png"
        attribute bow_none:
            "images/chrs/alina/layered_assets/clothes/bows/nonebow.png"

image alina_blink: 
    "images/chrs/alina/layered_assets/expressions/separate/eyes/open.png" 
    choice: 
        4.5 
    choice: 
        3.5 
    choice: 
        1.5 
    "images/chrs/alina/layered_assets/expressions/separate/eyes/closed.png" 
    .15 
    repeat
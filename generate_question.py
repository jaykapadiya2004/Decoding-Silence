import google.generativeai as genai
import os
from dotenv import load_dotenv
from util import *
import PIL


def generate_question(model, inp):
    message = '''Help me make a few questions out of the following passage. Include multiple choice questions, direct questions and answers, fill in the blanks and true and false questions. Also give me an answer for each question as well as some lines of exlpanation for each answer, and return it in JSON string'''
    num = 'let number of questions of each type be 2'
    message = message + inp + num

    response = model.generate_content(message, stream=True)
    response.resolve()
    text_file = open("Output.txt", "w")
    text_file.write(response.text)
    text_file.close()
    print(response.text)

# inp = '''
#     Despite their soft, gelatinous bodies, fossils thought to represent ctenophores, apparently with no tentacles but many more comb-rows than modern forms, have been found in lagerstätten as far back as the early Cambrian, about 515 million years ago. The position of the ctenophores in the evolutionary family tree of animals has long been debated, and the majority view at present, based on molecular phylogenetics, is that cnidarians and bilaterians are more closely related to each other than either is to ctenophores. A recent molecular phylogenetics analysis concluded that the common ancestor of all modern ctenophores was cydippid-like, and that all the modern groups appeared relatively recently, probably after the Cretaceous–Paleogene extinction event 66 million years ago. Evidence accumulating since the 1980s indicates that the cydippids are not monophyletic, in other words do not include all and only the descendants of a single common ancestor, because all the other traditional ctenophore groups are descendants of various cydippids.
#     Since its foundation, the Treaties sought to enable people to pursue their life goals in any country through free movement. Since its foundation, the Treaties sought to enable people to pursue their life goals in any country through free movement. Reflecting the economic nature of the project, the European Community originally focused upon free movement of workers: as a "factor of production". However, from the 1970s, this focus shifted towards developing a more "social" Europe. Free movement was increasingly based on "citizenship", so that people had rights to empower them to become economically and socially active, rather than economic activity being a precondition for rights. This means the basic "worker" rights in TFEU article 45 function as a specific expression of the general rights of citizens in TFEU articles 18 to 21. According to the Court of Justice, a "worker" is anybody who is economically active, which includes everyone in an employment relationship, "under the direction of another person" for "remuneration". A job, however, need not be paid in money for someone to be protected as a worker. For example, in Steymann v Staatssecretaris van Justitie, a German man claimed the right to residence in the Netherlands, while he volunteered plumbing and household duties in the Bhagwan community, which provided for everyone\'s material needs irrespective of their contributions. The Court of Justice held that Mr Steymann was entitled to stay, so long as there was at least an "indirect quid pro quo" for the work he did. Having "worker" status means protection against all forms of discrimination by governments, and employers, in access to employment, tax, and social security rights. By contrast a citizen, who is "any person having the nationality of a Member State" (TFEU article 20(1)), has rights to seek work, vote in local and European elections, but more restricted rights to claim social security. In practice, free movement has become politically contentious as nationalist political parties have manipulated fears about immigrants taking away people\'s jobs and benefits (paradoxically at the same time). Nevertheless, practically "all available research finds little impact" of "labour mobility on wages and employment of local workers".
#     The waxy cuticle of many leaves, the exoskeleton of insects, the shells and membranes of externally deposited eggs, and skin are examples of mechanical barriers that are the first line of defense against infection.
#     Several barriers protect organisms from infection, including mechanical, chemical, and biological barriers. The waxy cuticle of many leaves, the exoskeleton of insects, the shells and membranes of externally deposited eggs, and skin are examples of mechanical barriers that are the first line of defense against infection. However, as organisms cannot be completely sealed from their environments, other systems act to protect body openings such as the lungs, intestines, and the genitourinary tract. In the lungs, coughing and sneezing mechanically eject pathogens and other irritants from the respiratory tract. The flushing action of tears and urine also mechanically expels pathogens, while mucus secreted by the respiratory and gastrointestinal tract serves to trap and entangle microorganisms.'''
# print(main(model,inp))

def choice(choice, inp):
    load_dotenv()
    os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 50000,
    }
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)
    convo = model.start_chat(history=[
    ])
    output = ''
    if choice == 0:  # text imput
        output = generate_question(model, inp)
    elif choice == 1:  #  PIL text input
        output = util.ocr(inp)
    return output
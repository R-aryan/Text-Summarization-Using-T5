from services.text_summarization.application.ai.model import T5Model
from services.text_summarization.settings import Settings

t5_model = T5Model(model_name=Settings.MODEL_NAME, model_type=Settings.MODEL_TYPE)
t5_model.load_model(model_type=Settings.MODEL_TYPE,
                    use_gpu=Settings.USE_GPU,
                    model_path=Settings.WEIGHTS_PATH
                    )
# src = https://www.thehindu.com/business/Industry/twitter-interim-grievance-officer-for-india-quits/article35004295.ece
text_to_summarize = """summarize: Twitter’s interim resident grievance officer for India has stepped down, 
leaving the micro-blogging site without a grievance official as mandated by the new IT rules to address complaints 
from Indian subscribers, according to a source. 

The source said that Dharmendra Chatur, who was recently appointed as interim resident grievance officer for India by 
Twitter, has quit from the post. 

The social media company’s website no longer displays his name, as required under Information Technology (
Intermediary Guidelines and Digital Media Ethics Code) Rules 2021. 

Twitter declined to comment on the development.

The development comes at a time when the micro-blogging platform has been engaged in a tussle with the Indian 
government over the new social media rules. The government has slammed Twitter for deliberate defiance and failure to 
comply with the country’s new IT rules. """

result = t5_model.model.predict(text_to_summarize)
print(result)

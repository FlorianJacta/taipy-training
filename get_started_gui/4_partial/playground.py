# Write an app that create a card with all the information on the dictinary
from taipy.gui import Gui 
import taipy.gui.builder as tgb 

links = {"jobs": ["job1", "job2", "job3"],
         "experiences": ["exp1", "exp2", "exp3"],
         "links": ["https://www.linkedin.com/jobs/view/3838911071/?alternateChannel=search&refId=tgs%2BZonvkEQ%2Fehcct5tczw%3D%3D&trackingId=ZI6meYNLkfrI5cK9%2FomnnA%3D%3D", "https://www.linkedin.com/jobs/view/3856631906/?alternateChannel=search&refId=tgs%2BZonvkEQ%2Fehcct5tczw%3D%3D&trackingId=xfgMVHlUiLY8WeIYiZyNJQ%3D%3D", "https://www.linkedin.com/jobs/view/3856145801/?alternateChannel=search&refId=PcPkHtRnrabXTSanWBEg%2BQ%3D%3D&trackingId=s1SvCwhMp41Z04O2V4QXxw%3D%3D"]}


updated_links = {"jobs": ["job4", "job5", "job6"],
                "experiences": ["exp4", "exp5", "exp6"],
                "links": links["links"]}



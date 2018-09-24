import people_api_extractor as pae
import find_rice_people as frp


# Dan Wallach should be found in this article
# print(find_people(tagger, 'https://theconversation.com/4-ways-to-defend-democracy-and-protect-every-voters-ballot-101765'))


people_list = frp.find_people(tagger, 'https://theconversation.com/4-ways-to-defend-democracy-and-protect-every-voters-ballot-101765')
print(people_list)
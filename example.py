__author__ = 'francis'
import sys
import people_api as api
import cStringIO


def test(names):
    people = api.peopleType()
    for count, name in enumerate(names):
        id = '%d' % (count + 1, )
        person = api.personType(name=name, id=id)
        people.add_person(person)

    person = api.personType(name='mwaside',
                            id='76')
    agent = api.agentType("mwas")
    person.add_agent(agent)
    people.add_person(person)

    output = cStringIO.StringIO()
    people.export(output, 0, name_='people')

    xml_value = output.getvalue()
    output.close()
    return xml_value

print test(['albert', 'betsy', 'charlie'])
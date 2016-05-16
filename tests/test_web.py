import unittest
from random import randint

from tests.sharepoint_case import SPTestCase


class TestWeb(SPTestCase):
    new_web = None

    def test_can_create_web(self):
        web_prefix = str(randint(0, 100))
        creation_info = {'Url': "workspace" + web_prefix, 'Title': "Workspace"}
        new_web = self.context.web.webs.add(creation_info)
        self.context.execute_query()
        self.__class__.new_web = new_web

    def test_if_web_loaded(self):
        cur_web = self.__class__.new_web
        self.context.load(cur_web)
        self.context.execute_query()
        self.assertIsNotNone(cur_web, "Web resource was not requested")

    def test_if_web_updated(self):
        cur_web = self.__class__.new_web
        properties_to_update = {'Title': "New web site"}
        cur_web.update(properties_to_update)
        cur_web.context.execute_query()

        self.context.load(cur_web)
        self.context.execute_query()
        self.assertEquals(properties_to_update['Title'], cur_web.properties['Title'], "Web site update error")


if __name__ == '__main__':
    unittest.main()

from web.podemo2.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addMember1(self):
        username = 'aaai'
        accout = 'aaaai'
        phoneNum = '139000000013'
        addmember = self.main.goto_addmember1()
        addmember.add_member(username, accout, phoneNum)
        assert username in addmember.get_Member(username)

    def test_addMember(self):
        username = 'zc4pet45po'
        accout = 'zc54e45t'
        phoneNum = '13774556463'
        addmember = self.main.goto_contact().goto_addMember2()
        addmember.add_member(username, accout, phoneNum)
        assert addmember.get_Member(username)

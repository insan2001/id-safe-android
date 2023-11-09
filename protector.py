from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import Fernkey as fn
import process
import webbrowser as wb
from plyer import filechooser
from kivmob import KivMob

ads = KivMob("ca-app-pub-9320493450035769~5010087240")

location = ""
password = ""
key = ""
regex = ""
rst_doc = ""

privacy_policy = """
Privacy Policy
==============

Insan J built the ID SAFE app as an Ad Supported app. This SERVICE is provided by Insan J at no cost and is intended for use as is.

This page is used to inform visitors regarding my policies with the collection, use, and disclosure of Personal Information if anyone decided to use my Service.

If you choose to use my Service, then you agree to the collection and use of information in relation to this policy. The Personal Information that I collect is used for providing and improving the Service. I will not use or share your information with anyone except as described in this Privacy Policy.

The terms used in this Privacy Policy have the same meanings as in our Terms and Conditions, which is accessible at ID SAFE unless otherwise defined in this Privacy Policy.

Information Collection and Use

For a better experience, while using our Service, I may require you to provide us with certain personally identifiable information. The information that I request will be retained on your device and is not collected by me in any way.

The app does use third party services that may collect information used to identify you.

Link to privacy policy of third party service providers used by the app

Google Play Services
AdMob
Log Data

I want to inform you that whenever you use my Service, in a case of an error in the app I collect data and information (through third party products) on your phone called Log Data. This Log Data may include information such as your device Internet Protocol (“IP”) address, device name, operating system version, the configuration of the app when utilizing my Service, the time and date of your use of the Service, and other statistics.

Cookies

Cookies are files with a small amount of data that are commonly used as anonymous unique identifiers. These are sent to your browser from the websites that you visit and are stored on your device's internal memory.

This Service does not use these “cookies” explicitly. However, the app may use third party code and libraries that use “cookies” to collect information and improve their services. You have the option to either accept or refuse these cookies and know when a cookie is being sent to your device. If you choose to refuse our cookies, you may not be able to use some portions of this Service.

Service Providers

I may employ third-party companies and individuals due to the following reasons:

To facilitate our Service;
To provide the Service on our behalf;
To perform Service-related services; or
To assist us in analyzing how our Service is used.
I want to inform users of this Service that these third parties have access to your Personal Information. The reason is to perform the tasks assigned to them on our behalf. However, they are obligated not to disclose or use the information for any other purpose.

Security

I value your trust in providing us your Personal Information, thus we are striving to use commercially acceptable means of protecting it. But remember that no method of transmission over the internet, or method of electronic storage is 100% secure and reliable, and I cannot guarantee its absolute security.

Links to Other Sites

This Service may contain links to other sites. If you click on a third-party link, you will be directed to that site. Note that these external sites are not operated by me. Therefore, I strongly advise you to review the Privacy Policy of these websites. I have no control over and assume no responsibility for the content, privacy policies, or practices of any third-party sites or services.

Children’s Privacy

These Services do not address anyone under the age of 13. I do not knowingly collect personally identifiable information from children under 13. In the case I discover that a child under 13 has provided me with personal information, I immediately delete this from our servers. If you are a parent or guardian and you are aware that your child has provided us with personal information, please contact me so that I will be able to do necessary actions.

Changes to This Privacy Policy

I may update our Privacy Policy from time to time. Thus, you are advised to review this page periodically for any changes. I will notify you of any changes by posting the new Privacy Policy on this page.

This policy is effective as of 2021-01-30

Contact Us

If you have any questions or suggestions about my Privacy Policy, do not hesitate to contact me at insandc9683@gmail.com.

This privacy policy page was created at privacypolicytemplate.net and modified/generated by App Privacy Policy Generator

"""

terms = """
Terms & Conditions
==================

By downloading or using the app, these terms will automatically apply to you – you should make sure therefore that you read them carefully before using the app. You’re not allowed to copy, or modify the app, any part of the app, or our trademarks in any way. You’re not allowed to attempt to extract the source code of the app, and you also shouldn’t try to translate the app into other languages, or make derivative versions. The app itself, and all the trade marks, copyright, database rights and other intellectual property rights related to it, still belong to Insan J.

Insan J is committed to ensuring that the app is as useful and efficient as possible. For that reason, we reserve the right to make changes to the app or to charge for its services, at any time and for any reason. We will never charge you for the app or its services without making it very clear to you exactly what you’re paying for.

The ID SAFE app stores and processes personal data that you have provided to us, in order to provide my Service. It’s your responsibility to keep your phone and access to the app secure. We therefore recommend that you do not jailbreak or root your phone, which is the process of removing software restrictions and limitations imposed by the official operating system of your device. It could make your phone vulnerable to malware/viruses/malicious programs, compromise your phone’s security features and it could mean that the ID SAFE app won’t work properly or at all.

The app does use third party services that declare their own Terms and Conditions.

Link to Terms and Conditions of third party service providers used by the app

Google Play Services
AdMob
You should be aware that there are certain things that Insan J will not take responsibility for. Certain functions of the app will require the app to have an active internet connection. The connection can be Wi-Fi, or provided by your mobile network provider, but Insan J cannot take responsibility for the app not working at full functionality if you don’t have access to Wi-Fi, and you don’t have any of your data allowance left.

If you’re using the app outside of an area with Wi-Fi, you should remember that your terms of the agreement with your mobile network provider will still apply. As a result, you may be charged by your mobile provider for the cost of data for the duration of the connection while accessing the app, or other third party charges. In using the app, you’re accepting responsibility for any such charges, including roaming data charges if you use the app outside of your home territory (i.e. region or country) without turning off data roaming. If you are not the bill payer for the device on which you’re using the app, please be aware that we assume that you have received permission from the bill payer for using the app.

Along the same lines, Insan J cannot always take responsibility for the way you use the app i.e. You need to make sure that your device stays charged – if it runs out of battery and you can’t turn it on to avail the Service, Insan J cannot accept responsibility.

With respect to Insan J’s responsibility for your use of the app, when you’re using the app, it’s important to bear in mind that although we endeavour to ensure that it is updated and correct at all times, we do rely on third parties to provide information to us so that we can make it available to you. Insan J accepts no liability for any loss, direct or indirect, you experience as a result of relying wholly on this functionality of the app.

At some point, we may wish to update the app. The app is currently available on Android – the requirements for system(and for any additional systems we decide to extend the availability of the app to) may change, and you’ll need to download the updates if you want to keep using the app. Insan J does not promise that it will always update the app so that it is relevant to you and/or works with the Android version that you have installed on your device. However, you promise to always accept updates to the application when offered to you, We may also wish to stop providing the app, and may terminate use of it at any time without giving notice of termination to you. Unless we tell you otherwise, upon any termination, (a) the rights and licenses granted to you in these terms will end; (b) you must stop using the app, and (if needed) delete it from your device.

Changes to This Terms and Conditions

I may update our Terms and Conditions from time to time. Thus, you are advised to review this page periodically for any changes. I will notify you of any changes by posting the new Terms and Conditions on this page.

These terms and conditions are effective as of 2021-01-30

Contact Us

If you have any questions or suggestions about my Terms and Conditions, do not hesitate to contact me at insandc9683@gmail.com.

This Terms and Conditions page was generated by App Privacy Policy Generator

"""

enc_dec = """
sample

"""
ads.new_interstitial("ca-app-pub-9320493450035769/2235588393")


def SwitchToFCS():
    FCS = FileChooserScreen(name="file")
    sm.switch_to(FCS, direction="up")
    ads.request_interstitial()
    ads.show_interstitial()

class WindowManager(ScreenManager):
    pass

class FileChooserScreen(Screen):

    def file(self):
        global location
        loc = filechooser.open_file()
        if loc:
            location = loc[0]
            pattern = fn.fernkey_finder(location)
            if pattern:
                ps_text = "This File Already Encrypted.\nPut The Correct Password\nFor This File To Decrypt"
                ps_btn = "Decrypt"
            else:
                ps_text = "This File Not Encrypted.\nPut A Password For Encrypt."
                ps_btn = "Encrypt"

            ps = PasswordScreen()
            sm.switch_to(ps, direction="left")
            ps.update_label(ps_text, ps_btn)

class MyButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = 'images/menu_bar.png'

class PasswordScreen(Screen):
    left_arrow = "images/menu_bar.png"
    label = ObjectProperty(None)
    btn = ObjectProperty(None)

    def update_label(self, ps_text, ps_btn):
        self.label.text = ps_text
        self.btn.text = ps_btn

    def encrypt(self):
        process.encrypt(location, password)
        sm.switch_to(EncryptionCompleteScreen(name="encinfo"), direction="left")
        ads.request_interstitial()
        ads.show_interstitial()

    def decrypt(self):
        process.decrypt(key, regex, location)
        sm.switch_to(DecryptionCompleteScreen(name="decinfo"), direction="left")
        ads.request_interstitial()
        ads.show_interstitial()

    def function(self, passwd):
        global password, key, regex
        if not passwd:
            sm.switch_to(ErrorScreen(name="error"), direction="down")
        elif not len(passwd) >= 4:
            sm.switch_to(LenErrorScreen(name="len_error"), direction="down")
        else:
            password = passwd
            key, regex, data_file = fn.regex_to_key(location, password)
            if not key:
                self.encrypt()
            else:
                self.decrypt()

class LenErrorScreen(Screen):
    pass

class ErrorScreen(Screen):
    error_img = "images/error.png"
    label_text = "You Must Enter A One Time Password To Continue." \
        "This Password Used In Only Next Process."

    def submit(self):
        sm.switch_to(PasswordScreen(name="password"), direction="up")

class AboutScreen(Screen):
    right_arrow = "images/menu_bar.png"

class EncryptionCompleteScreen(Screen):
    reveal_password = ""
    message = "Now Your File Fully\nEncrypted.Everyone \nCan Use This" \
              "File With\nOut Your Password."

    def show_password(self):
        self.reveal_password = f"Your Password For \n{location}\nis\n" \
                          f"{password}"

        self.ids.show.text = self.reveal_password

    def Home(self):
        SwitchToFCS()

class DecryptionCompleteScreen(Screen):
    message = "Now Your File Sucessfully\nDecrypted." \
              "Now You Can Use\nThis File As Normal."
    note = "After Using This File\nEncrypt For Safty Purpose."

    def Home(self):
        SwitchToFCS()

class AboutMe(Screen):

    social_media = ""
    facebook = "https://www.facebook.com/groups/1167258160360107"
    youtube = "https://urlgeni.us/youtube/channel/saampaar"
    blogger = "https://individualcreat.blogspot.com/"
    paypal = "https://www.paypal.com/donate?hosted_button_id=7FQXN562FPEN6"

    blogger_img = "images/blogger.png"
    fb_img = "images/facebook.png"
    youtube_img = "images/youtube.png"
    paypal_img = "images/paypal.png"
    me = "images/me.jpeg"

    def socialmedia(self):
        if self.social_media == "youtube":
            wb.open(self.youtube)
        elif self.social_media == "facebook":
            wb.open(self.facebook)
        elif self.social_media == "blogger":
            wb.open(self.blogger)
        elif self.social_media == "paypal":
            wb.open(self.paypal)

class TempScreen(Screen):

    label = ObjectProperty(None)

    def update_label(self, ps_text):
        self.label.text = ps_text

    def sub(self):
        sm.switch_to(AboutApp(name="app"), direction="up")

class AboutApp(Screen):


    def rst_text(self, type):
        global rst_doc
        TS = TempScreen(name="temp")
        if type == "policy":
            sm.switch_to(TS, direction="down")
            TS.update_label(privacy_policy)
        elif type == "terms":
            sm.switch_to(TS, direction="down")
            TS.update_label(terms)
        elif type == "process":
            rst_doc = enc_dec
            sm.switch_to(TS, direction="down")
            TS.update_label(enc_dec)


kv = Builder.load_file("protector.kv")
sm = WindowManager()

screens = [FileChooserScreen(name="file"),
           AboutScreen(name="about"),
           PasswordScreen(name="password"),
           ErrorScreen(name="error"),
           EncryptionCompleteScreen(name="encinfo"),
           DecryptionCompleteScreen(name="decinfo"),
           AboutApp(name="app"),
           AboutMe(name="me"),
           LenErrorScreen(name="len_error"),
           TempScreen(name="temp")
           ]

for screen in screens:
    sm.add_widget(screen)

sm.current = "file"

class ProtectorApp(App):
    def build(self):
        self.title = "ID SAFE"
        ads.new_interstitial("ca-app-pub-9320493450035769/2235588393")
        ads.request_interstitial()
        ads.show_interstitial()
        return sm

app = ProtectorApp()
app.run()

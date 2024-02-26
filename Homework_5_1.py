# class A:
#     def __init__(self, default_x):
#         self.x = default_x
#
#     def my_name(self):
#         print(f'My name is class A and {self.x}')
#
#     def test_func(self):
#         self.my_name()
#
#
# # a = A(12)
# # a.my_name()
# # a.test_func()
# # print(a.x)
#
# class Publication:
#     def __init__(self, name='Test name'):
#         self.name = name
#
#     def publish_date(self):
#         print(self.__calculate_date())
#
#     def __calculate_date(self):
#         return 'date'
#
#     def publish(self):
#         pass
#
# pub = Publication('Today news')
# # print(pub.name)
#
#
# class Video:
#     def __init__(self, quality='720'):
#         self.quality = quality
#
#     def show_quality(self):
#         print(f'Quality is {self.quality}')
#
#     def publish(self):
#         self.__set_quality()
#         self.__upload_youtube()
#         self.__add_subtitles
#
#
# class Advertising(Publication):
#     def __init__(self, name, customer):
#         Publication.__init__(self, name=name)
#         self.customer = customer
#     def who_is_customer(self):
#         print(f'Customer is {self.customer}')
#
#     def publish(self):
#         self.__set_customer()
#         self.__set_date_until()
#
#
# adv = Advertising('Ad_name', 'Google')
# # print(adv.name)
# # adv.who_is_customer()
# # adv.publish_date()
#
# class Movie(Publication, Video):
#     def __init__(self, name, quality):
#         Publication.__init__(self, name=name)
#         Video.__init__(self, quality=quality)
#         # super().__init__()
#         self.director = 'Cameron'
#
#     def publish(self):
#         self.__add_to_site()
#
#
# movie = Movie('Terminator', 1080)
# movie.show_quality()
# print(movie.name)
# movie.publish_date()
# print(movie.director)
#
# movie.publish()
# adv.publish()
# pub.publish()
#
# import re
# from re import findall
# from time import *
# from time import sleep as sleep

print('Hello')
a = 5

if __name__ == '__main__':
    print('Only from module')

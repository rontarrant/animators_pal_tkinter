from borg_idiom_preferences_singleton import Preferences

a = Preferences()
print("a: ", a)
c = Preferences()
print("a: ", a, " c: ", c)
#a.fps = 18
print(f"fps: {c.fps}")
print("a: ", a, " c: ", c)


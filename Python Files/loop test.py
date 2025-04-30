the_burger = 16.99;
french_fries = 5.99;
currie_sauce = 19.99;
napkins_with_chocolates = 10.50;
juice_box = 89.01;
takeout = 18.99;
total = 0.0;
DONE = False
print("""
+-------------------------------------------+
| The Restaurant at the End of the Universe |
+---------------------------------+---------+
| A\tThe "Big Boy" Burger      | $""" + str(the_burger) + """  |
+---------------------------------+---------+
| B\tFrench Fries              | $""" + str(french_fries) + """   |
+---------------------------------+---------+
| C\tCurrie sauce              | $""" + str(currie_sauce) + """  |
+---------------------------------+---------+
| D\tNapkins with Chocolates   | $""" + str(napkins_with_chocolates) + str(0) + """  |
+---------------------------------+---------+
| E\tJuice Box                 | $""" + str(juice_box) + """  |
+---------------------------------+---------+
| F\tTakeout                   | $""" + str(takeout) + """  |
+---------------------------------+---------+
""");
while(not DONE):
  print("Total:", total);
  Item = input("Select a letter or 'done': ");
  if Item is "A":
    total += the_burger;
  elif Item is "B":
    total += french_fries;
  elif Item is "C":
    total += currie_sauce;
  elif Item is "D":
    total += napkins_with_chocolates;
  elif Item is "E":
    total += juice_box;
  elif Item is "F":
    total += takeout;
  elif Item is "done":
    print("Final total:", total);
    DONE = True


def main():
    order = get_order()


if __name__ == "__main__":
    main()
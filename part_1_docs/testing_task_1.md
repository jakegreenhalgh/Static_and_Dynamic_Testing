### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  def check_for_ace(self, card):
    if card.value = 1: #needs two '='
      return True
    else #has not added ':' after else
      return False
   

  dif highest_card(self, card1 card2): #'dif' not 'def', no comma after card card1
  if card1.value > card2.value: #indentaion not correct
    return card #should be card1
  else:
    return card2
  


def cards_total(self, cards): #incorrect indentation
  total #needs to state the value of the variable 'total'
  for card in cards:
    total += card.value
    return "You have a total of" + total #need to convert the total to a str before concatenation, missing space at end, return indented within loop
  
```

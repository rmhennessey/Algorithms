#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batch = {} #create empty dict that we are going to return
    for key, value in recipe.items(): #look at key value pairs in the recipe dictionary
        if key not in ingredients: #if ingredients does not have the recipe key, you cannot make it
            return 0 # so return 0 - base case
        batch[key] = ingredients[key] // value 
    print((batch, min(batch.values())))
    return min(batch.values())


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
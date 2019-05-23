# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:14:55 2019

@author: GELab
"""

import requests
import json
import html2text

HEADERS = {
    'X-RapidAPI-Host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com',
    'X-RapidAPI-Key': 'cf57e086cfmsh8dc753c16660113p1c2690jsn8884bcdae13a',
}

params = (
    ('number', '2'),
    ('ranking', '1'),
    ('ignorePantry', 'false'),
    ('ingredients', 'apples,flour,sugar'),
)

response = requests.get('https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients', headers=HEADERS, params=params)

jsonData = json.loads(response.text)
len(jsonData)

def getSuggestedRecipe(ingredientsDict):
    
    
    ingredientsStr = ','.join(ingredientsDict.keys())
    
    params = (
    ('number', '1'),
    ('ranking', '1'),
    ('ignorePantry', 'false'),
    ('ingredients',ingredientsStr ),
    )
    
    
    responseByIng = requests.get('https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients', headers=HEADERS, params=params)

    jsonData = json.loads(responseByIng.text)
    
    
    topRecipe = jsonData[0]['title']
    topRecipeID = str(jsonData[0]['id'])
    
    responseRecipeSumm = requests.get('https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/'+topRecipeID+'/summary',
                            headers=HEADERS)
    
    jsonData = json.loads(responseRecipeSumm.text)
    topRecipeSumm = jsonData['summary']
    
    return topRecipe,topRecipeSumm


if __name__ == '__main__':
    
    result = getSuggestedRecipe({'apple': 3, 'carrot': 1,'cucumber':2})
    
    print(html2text.html2text(result[1]))

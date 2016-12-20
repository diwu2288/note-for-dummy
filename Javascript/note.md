**To parse JSON object to JS object**

`var jsObj = JSON.parse(jsonObj);`

**Get the number of items under a \<ul\> element

`("#id_of_ul").children.length`

**To convert part of the object array to a new array
```
var countryLang = [
  {country: 'se', lang: 'sv'},
  {country: 'gb', lang: 'en'}
]
var countries = countryLang.map(function(obj){return obj.country})
```

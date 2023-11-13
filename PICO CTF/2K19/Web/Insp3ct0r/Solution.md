# Write Up for Web Exploit challenge for PICO CTF 2K19 - Insp3ct0r 

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Kishor Balan tipped us off that the following code may need inspection:\
https://jupiter.challenges.picoctf.org/problem/41511/ or http://jupiter.challenges.picoctf.org:41511

[WebSite Main Page](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/Insp3ct0r/website.png)

## FLAG PART 1/3

In the **Page-Source** of main source. Inform of HTML comment

```html
<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
```

Refer: [See this](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/Insp3ct0r/images/page_source.png)

## FLAG PART 2/3

In the page source of css file found in previous page source. 

```css
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
```

Refer: [See this](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/Insp3ct0r/images/css.png)

## FLAG PART 3/3

In the page source of js file found in previous page source. 

```js
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?832b0699} */
```

Refer: [See this](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/Insp3ct0r/images/js.png)


## FLAG

picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}

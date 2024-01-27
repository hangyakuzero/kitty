# Kitty
![kitty](https://github.com/hangyakuzero/kitty/assets/46108879/12065f28-b4e4-49b2-af49-6d1da3473c06)<br>
A python-cli tool to encode text/payloads into base64, url, hex ,octal and alternating text
 
# Usage
1.`python3 kitty.py encrypt [encoding type] "text to encode"`
it currently supports hex,octal,url , base 64, and alternating, it also has an 'all' flag 

2.multiple lines with Xargs:
`cat test.txt | xargs -I {} python3 kitty.py encrypt all "{}"`
## sample output
<img width="676" alt="Screenshot 2024-01-27 at 11 27 41 PM" src="https://github.com/hangyakuzero/kitty/assets/46108879/61d02dae-7a0f-4cce-803a-41f4346388a5">
<br>with Xargs:<br><br>
                     
<img width="531" alt="Screenshot 2024-01-27 at 11 30 44 PM" src="https://github.com/hangyakuzero/kitty/assets/46108879/6130e6c3-3029-4f77-a024-0b2d89925448">

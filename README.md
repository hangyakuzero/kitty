# kitty
A python-cli tool to encode text/payloads into base64, url, hex and octal

# Usage
1.`python3 kitty.py encrypt [encoding type] "text to encode"`
it currently supports hex,octal,url and base 64, it also has an 'all' flag 

2.multiple lines with Xargs:
`cat test.txt | xargs -I {} python3 kitty.py encrypt all "{}"`
## sample output
<img width="639" alt="Screenshot 2024-01-21 at 12 45 21 AM" src="https://github.com/hangyakuzero/kitty/assets/46108879/45b7dd31-48dc-4721-a075-8d92a297e57b"><br>
         <br>with Xargs:<br><br>
<img width="548" alt="Screenshot 2024-01-21 at 12 44 06 AM" src="https://github.com/hangyakuzero/kitty/assets/46108879/8e9f2552-439a-40f7-9b7c-705a3a2bd86e">
                     

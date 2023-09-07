from googlesearch import search
import colorama
import GoogleLogo as gl

google_text = gl.google_text

UP = '\033[1A'
CLEAR = '\x1b[2K'

print(google_text)
print(f'\t {gl.colors.ENDC}')

# print(UP, end=CLEAR)
print(f'\t {gl.colors.CYAN} {gl.colors.ENDC}')
colorama.init()
# print(colorama.Fore.BLUE + 'G' + colorama.Fore.RED + 'O' + colorama.Fore.YELLOW + 'O' + colorama.Fore.BLUE + 'G' +
# colorama.Fore.GREEN + 'L' + colorama.Fore.RED + 'E') print(bold('\n\n\t\t\t\t{0}G{1}O{2}O{3}G{4}L{5}E'.format(
# colorama.Fore.BLUE, colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.GREEN,
# colorama.Fore.RED)))

ender: str = input('{0}\t ENTER YOUR SEARCH: '.format(colorama.Fore.WHITE))
print(f'\t\t\n\n{colorama.Fore.GREEN}{"sorry, wait we will carry out your requests...".upper()}')

for query in search(ender, tld='com', num=50, stop=50, pause=15, lang='all'):
    print(colorama.Fore.GREEN + '[*]', colorama.Fore.WHITE + query)
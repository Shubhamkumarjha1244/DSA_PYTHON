def reverse(main,help):
    if not main:
        return
    temp=main[-1]
    main.pop()
    reverse(main,help)
    while main:
        help.append(main.pop())
    main.append(temp)
    while help:
        main.append(help.pop())





help=[]
main=[1,2,3,4]
print('Original Stack--',main)
reverse(main,help)
print('reverse Stack--',main)
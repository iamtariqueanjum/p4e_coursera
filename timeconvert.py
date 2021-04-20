hour = int(input("Starting time (hours): ")) #0.......23
mins = int(input("Starting time (minutes): ")) #0.......59
dura = int(input("Event duration (minutes): "))

endhour = hour + (dura // 60) 
endmins = mins + (dura % 60)
endhour += endmins // 60
endmins = endmins % 60
endhour = endhour % 24 

print('{}:{}'.format(endhour, endmins))
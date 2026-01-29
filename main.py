from pyscript import display, document

def intrams_checker(e):
    registration = document.querySelector("input[name='registration']:checked").value
    clearance = document.querySelector("input[name='clinic']:checked").value

    if registration == 'yes' and clearance == 'yes':
        display("You are allowed to take the intrams.", target='output')
    else:
        display("You are not allowed to take the intrams.", target='output')

document.getElementById('button').addEventListener('click', intrams_checker)
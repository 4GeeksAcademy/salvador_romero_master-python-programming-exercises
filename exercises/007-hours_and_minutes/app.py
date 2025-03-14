def hours_minutes(seconds):
  # Your code here
  horas = int(seconds/3600)
  minutos = int((seconds%3600)/60)
  return (horas,minutos)

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))

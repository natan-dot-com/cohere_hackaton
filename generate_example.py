import cohere
co = cohere.Client('Xcg9JtDmsEmVaYt6THBdm6Q8QgrMRWi2PMCRa7JU')

response = co.generate(
  prompt='Please explain to me how LLMs work',
)
print(response)
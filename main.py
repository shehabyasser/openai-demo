from openai import OpenAI

client = OpenAI(api_key='')

def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    prompt = "Write a poem about the Seattle."
    response = generate_response(prompt)
    print(response)


###
# In Seattle's misty morning light,
# Where mountains touch the sky so bright,
# The city by the sea so fair,
# With culture, art, and coffee rare.

# Rain falls softly, whispers sweet,
# Upon the streets beneath our feet,
# Pike Place Market's bustling charm,
# Where vendors call and tourists swarm.

# The Space Needle stands tall and proud,
# A beacon in the bustling crowd,
# Reflecting all the city's grace,
# A symbol of this special place.

# From music scene to tech's advance,
# Seattle's spirit will entrance,
# A blend of old and new, you'll find,
# In this city, so unconfined.

# So visit Seattle, come and see,
# The beauty of the emerald city,
# Where nature's wonders intertwine,
# With urban life in perfect rhyme.
###

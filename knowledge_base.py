rules = [
    # If an entity has feathers and can fly, infer it might be an animal (for more flexible subject names)
    {
        "conditions": [
            ("has_property", "X", "feathers"),
            ("can", "X", "fly")
        ],
        "conclusion": ("is_a", "X", "animal")
    },
    # If an entity is an animal, has feathers, and can fly, infer it might be a bird
    {
        "conditions": [
            ("is_a", "X", "animal"),
            ("has_property", "X", "feathers"),
            ("can", "X", "fly")
        ],
        "conclusion": ("hypothesis", "X", "might_be_a_bird")
    },
    {
        "conditions": [
            ("has_property", "X", "feathers"),
            ("can", "X", "fly"),
            ("is_a", "X", "animal")
        ],
        "conclusion": ("hypothesis", "X", "might_be_a_bird")
    },
    {
        "conditions": [
            ("has_property", "X", "arms"),
            ("can", "X", "swim")
        ],
        "conclusion": ("hypothesis", "X", "might_be_an_aquatic_animal")
    },
    {
        "conditions": [
            ("has_property", "X", "metal"),
            ("can", "X", "conduct_electricity")
        ],
        "conclusion": ("hypothesis", "X", "might_be_a_conductor")
    },
    {
        "conditions": [
            ("has_property", "X", "substance"),
            ("boils_at", "X", "100C")
        ],
        "conclusion": ("hypothesis", "X", "might_be_water")
    },
    {
        "conditions": [
            ("is_a", "X", "sky"),
            ("has_property", "X", "dark"),
            ("makes_sound", "X", "rumbling")
        ],
        "conclusion": ("hypothesis", "X", "might_be_rain")
    },
    {
        "conditions": [
            ("is_a", "X", "plant"),
            ("has_property", "X", "green"),
            ("can", "X", "use_sunlight")
        ],
        "conclusion": ("hypothesis", "X", "might_be_photosynthesizing")
    },
    {
        "conditions": [
            ("is_a", "X", "human"),
            ("has_symptom", "X", "sneezing"),
            ("has_symptom", "X", "coughing"),
            ("has_symptom", "X", "fever")
        ],
        "conclusion": ("hypothesis", "X", "might_have_flu")
    },
    {
        "conditions": [
            ("is_a", "X", "object"),
            ("has_part", "X", "wheels"),
            ("has_part", "X", "engine"),
            ("has_part", "X", "seats")
        ],
        "conclusion": ("hypothesis", "X", "might_be_a_vehicle")
    }
]

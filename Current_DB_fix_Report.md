# Airbnb Analytics - Current Database Fix Report

This report documents the status of all 6 core queries after the comprehensive fix for empty results, missing fields, and JSON serialization errors.

## [Query 1] Portland 2-Day Search (Feb 23-24)
**Engine**: Mongo MQL
**Endpoint**: `/api/dashboard/portland_search`

### Full JSON Output
```json
[
  {
    "accommodates": 2,
    "id": 1459773359905874906,
    "name": "90s-Theme Studio, Treetop Views, 7 Min to Downtown",
    "neighborhood": "Overlook",
    "price": 103.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 30591779,
    "name": "Private room in SE",
    "neighborhood": "Brentwood-Darlington",
    "price": 50.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "id": 34123760,
    "name": "Cedar House",
    "neighborhood": "Boise",
    "price": 76.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 1394997995332128546,
    "name": "Cozy, Historic, Portland home.",
    "neighborhood": "Irvington",
    "price": 92.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 1283568174210420936,
    "name": "Studio 1 Bath, OHSU, Dog Friendly (04E)",
    "neighborhood": "Homestead",
    "price": 148.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 728393926601096854,
    "name": "Private Room in walkable SE Portland -UNIT A",
    "neighborhood": "Mt. Scott-Arleta",
    "price": 63.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 4,
    "id": 43612262,
    "name": "Mt. Tabor/ SE Portland Modern Warmth",
    "neighborhood": "South Tabor",
    "price": 162.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 9,
    "id": 40122072,
    "name": "Charming home in safe beautiful area - fenced yard",
    "neighborhood": "Northwest Heights",
    "price": 286.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 855692533793103757,
    "name": "Hawthorne Schoolhouse",
    "neighborhood": "Richmond",
    "price": 129.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 16,
    "id": 1001627335081881662,
    "name": "Family + Pet-friendly, sleeps 16",
    "neighborhood": "Cully",
    "price": 392.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 22173141,
    "name": "Light filled basement apartment",
    "neighborhood": "Piedmont",
    "price": 100.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 6,
    "id": 1342382998636626411,
    "name": "NE PDX Blue Bungalow",
    "neighborhood": "Concordia",
    "price": 131.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 31284993,
    "name": "Luxury Apartment For Rent",
    "neighborhood": "Irvington",
    "price": 199.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 929266002843301947,
    "name": "Private room and Bath in downtown Portland",
    "neighborhood": "Portland Downtown",
    "price": 60.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "id": 1356115369955926944,
    "name": "2 bd townhome near Nike/Intel with 5 star ratings",
    "neighborhood": "Bridlemile",
    "price": 110.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 882516112627638676,
    "name": "Modern Apartment in Portland's Pearl District",
    "neighborhood": "Pearl",
    "price": 151.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 51351075,
    "name": "Guest house with lots of natural light",
    "neighborhood": "North Tabor",
    "price": 75.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "id": 1420370673669429204,
    "name": "Charming 2BR Apartment – Walk to Alberta",
    "neighborhood": "Sabin",
    "price": 123.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "id": 1331428927604071993,
    "name": "South Tabor Charmer",
    "neighborhood": "South Tabor",
    "price": 194.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 1104340170176037493,
    "name": "Bright! Modern! South-facing studio with views!",
    "neighborhood": "Pearl",
    "price": 65.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "id": 1258727634110216045,
    "name": "Stunning  Mt Tabor Gem Custom Designed",
    "neighborhood": "Mt. Tabor",
    "price": 167.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 6,
    "id": 1340612886009795405,
    "name": "Centrally Located Portland Home: Pets Welcome!",
    "neighborhood": "North Tabor",
    "price": 174.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 750260372351835719,
    "name": "The Loft; N. Portland",
    "neighborhood": "Portsmouth",
    "price": 102.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 7,
    "id": 630606067983802554,
    "name": "Fenced Yard! Pet Friendly, 3 Bedroom, no fees",
    "neighborhood": "South Portland",
    "price": 200.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 1404417592973852280,
    "name": "Overlook Bungalow Near N. Mississippi Avenue",
    "neighborhood": "Overlook",
    "price": 155.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 1,
    "id": 588293421871372350,
    "name": "Hazelwood getaway in NE Portland #1",
    "neighborhood": "Hazelwood",
    "price": 30.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "id": 1091413309953163811,
    "name": "Best Neighborhood in Town! #9",
    "neighborhood": "Northwest District",
    "price": 64.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 716148753790021423,
    "name": "Vintage Cottage in NE Portland",
    "neighborhood": "Concordia",
    "price": 91.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 6,
    "id": 1450192807760377257,
    "name": "Great House for your enjoyment",
    "neighborhood": "Pleasant Valley",
    "price": 169.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 1210936356869152861,
    "name": "2BR Historic Soul District Remodel",
    "neighborhood": "Eliot",
    "price": 211.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 47779834,
    "name": "Riposo: A private artistic getaway",
    "neighborhood": "King",
    "price": 92.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 23432611,
    "name": "Master Suite + 1 BR in N. Mississippi District.",
    "neighborhood": "Piedmont",
    "price": 152.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 3,
    "id": 1376920908849903700,
    "name": "Sweet Suite - Private Studio",
    "neighborhood": "South Tabor",
    "price": 90.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 10,
    "id": 16416965,
    "name": "Private Modern Portland Home - KING BED",
    "neighborhood": "West Portland Park",
    "price": 350.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "id": 1379908675113767176,
    "name": "Modern house, home theater",
    "neighborhood": "Glenfair",
    "price": 285.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "id": 42878671,
    "name": "Modern Portland  Craftsman in heart of Mississippi",
    "neighborhood": "Boise",
    "price": 368.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 29181876,
    "name": "Marianna Condo",
    "neighborhood": "South Portland",
    "price": 104.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 6,
    "id": 1311027511553756518,
    "name": "Irvington Bungalow",
    "neighborhood": "Grant Park",
    "price": 145.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 9,
    "id": 1424292690323545154,
    "name": "Nob Hill Nest",
    "neighborhood": "Northwest District",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 51260916,
    "name": "St. Johns Apartment 2 Bed 1 Bath",
    "neighborhood": "St. Johns",
    "price": 70.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 27362354,
    "name": "Backyard Garden Retreat",
    "neighborhood": "Reed",
    "price": 81.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "id": 49117607,
    "name": "Oswego Empty Nest",
    "neighborhood": "Arnold Creek",
    "price": 96.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 1254019089032383954,
    "name": "Stylish 2BR Duplex Near Alberta Arts District",
    "neighborhood": "Concordia",
    "price": 208.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 16,
    "id": 635413907290834919,
    "name": "Astroranchpdx  7acres, 20 min from central PDX",
    "neighborhood": "Pleasant Valley",
    "price": 311.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 51422753,
    "name": "River view, rooftop deck, 2bd 2ba",
    "neighborhood": "Old Town/Chinatown",
    "price": 119.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 563223799929727708,
    "name": "Cozy Vintage Pub Theme 1 bd w/ private entrance",
    "neighborhood": "Lents",
    "price": 66.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 15,
    "id": 40864982,
    "name": "Amazing location, family friendly in Alberta Arts",
    "neighborhood": "Vernon",
    "price": 644.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 552459643994124868,
    "name": "Downtown next to the Pearl, Providence Park & NW",
    "neighborhood": "Goose Hollow",
    "price": 70.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 4648534,
    "name": "The perfect spot!",
    "neighborhood": "Sellwood-Moreland Improvement League",
    "price": 75.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 1061146794606232217,
    "name": "Lavender Farm Stay at Urban Donkey Studio",
    "neighborhood": "Sunderland",
    "price": 339.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  }
]
```

---

## [Query 2] Portland: Most Competitive Markets (Density)
**Engine**: Mongo MQL
**Endpoint**: `/api/dashboard/no_vacancy`

### Full JSON Output
```json
[
  {
    "avg_price": 159.07,
    "avg_rating": 0,
    "booked_count": 247,
    "neighborhood": "Northwest District"
  },
  {
    "avg_price": 112.77,
    "avg_rating": 0,
    "booked_count": 215,
    "neighborhood": "Richmond"
  },
  {
    "avg_price": 4269.63,
    "avg_rating": 0,
    "booked_count": 206,
    "neighborhood": "Portland Downtown"
  },
  {
    "avg_price": 2049.61,
    "avg_rating": 0,
    "booked_count": 178,
    "neighborhood": "Buckman"
  },
  {
    "avg_price": 140.48,
    "avg_rating": 0,
    "booked_count": 145,
    "neighborhood": "Concordia"
  },
  {
    "avg_price": 124.59,
    "avg_rating": 0,
    "booked_count": 135,
    "neighborhood": "King"
  },
  {
    "avg_price": 159.44,
    "avg_rating": 0,
    "booked_count": 133,
    "neighborhood": "Hosford-Abernethy"
  },
  {
    "avg_price": 126.92,
    "avg_rating": 0,
    "booked_count": 131,
    "neighborhood": "Boise"
  },
  {
    "avg_price": 144.37,
    "avg_rating": 0,
    "booked_count": 121,
    "neighborhood": "Sunnyside"
  },
  {
    "avg_price": 177.23,
    "avg_rating": 0,
    "booked_count": 118,
    "neighborhood": "Kerns"
  }
]
```

---

## [Query 3] Salem: Top-Rated Listings
**Engine**: Mongo MQL
**Endpoint**: `/api/dashboard/salem_booking`

### Full JSON Output
```json
[
  {
    "accommodates": 1,
    "name": "Quiet Residential Home For Traveling Nurses",
    "neighborhood": "Ward 4",
    "price": 30.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 7,
    "name": "Basement Paradise Entire house",
    "neighborhood": "Ward 8",
    "price": 165.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "name": "Bright bungalow, pet-friendly, fenced yard",
    "neighborhood": "Ward 2",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 6,
    "name": "Historic Home Near Downtown Salem: Walk to Capitol",
    "neighborhood": "Ward 1",
    "price": 224.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 7,
    "name": "Big Blue* Extended stay ~ Family & Pet Friendly!",
    "neighborhood": "Ward 8",
    "price": 195.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "1 Bedroom Home in a New South Salem Community",
    "neighborhood": "Ward 3",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "Mid-Century Guest House",
    "neighborhood": "Ward 3",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "Ms. Lorraine's Boarding House Red Room",
    "neighborhood": "Ward 2",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "name": "Charming Historic Bungalow",
    "neighborhood": "Ward 1",
    "price": 68.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "Lovely 1-bedroom unit in the West Hills",
    "neighborhood": "Ward 8",
    "price": 60.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "Sunlit Mini-Suite  near Willamette University",
    "neighborhood": "Ward 7",
    "price": 68.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "name": "1  Cozy flat w/ office.  Garden/creek views",
    "neighborhood": "Ward 2",
    "price": 98.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "name": "Single Level, Modern, Clean 3 Bdrm 2 Bath Property",
    "neighborhood": "Ward 7",
    "price": 233.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 1,
    "name": "*Quiet Residential Home For Traveling Nurses",
    "neighborhood": "Ward 4",
    "price": 30.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 4,
    "name": "Two side-by-side apartments",
    "neighborhood": "Ward 2",
    "price": 164.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "name": "Historic Cottage close to downtown for Eclipse",
    "neighborhood": "Ward 1",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 6,
    "name": "Historic Italianate Charm",
    "neighborhood": "Ward 2",
    "price": 188.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "name": "Beautiful Fully Furnished 3 bedroom 2 bath home",
    "neighborhood": "Ward 7",
    "price": 74.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "name": "Hidden Gem Downtown Salem Private Bath & Room",
    "neighborhood": "Ward 1",
    "price": 51.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "name": "Spacious and bright private master bedroom.",
    "neighborhood": "Ward 7",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "name": "Charming Vintage Home",
    "neighborhood": "Ward 1",
    "price": 135.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "name": "Monthly Downtown Salem Loft Apt. by Salemstays.com",
    "neighborhood": "Ward 1",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 1,
    "name": "S. Salem Quiet Bedroom",
    "neighborhood": "Ward 4",
    "price": 28.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 1,
    "name": "Single room in Comfort Home",
    "neighborhood": "Ward 7",
    "price": 54.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "name": "Warm and welcoming private bedroom.",
    "neighborhood": "Ward 7",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 8,
    "name": "3rd Generation Farmhouse; 4 bdrm, 3.5 bath",
    "neighborhood": "Ward 7",
    "price": 475.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 1,
    "name": "Handsome Mini-suite near Willamette University",
    "neighborhood": "Ward 2",
    "price": 69.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 5,
    "name": "Gorgeous 3 bedroom pet friendly home - West Salem",
    "neighborhood": "Ward 8",
    "price": 135.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "West Salem: Relax, Refresh and Room to sprawl",
    "neighborhood": "Ward 8",
    "price": 76.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 1,
    "name": "Modern bedroom Ideal For Long Term Stay.",
    "neighborhood": "Ward 3",
    "price": 47.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 1,
    "name": "South Salem private room.",
    "neighborhood": "Ward 2",
    "price": 38.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 4,
    "name": "Perfect Home for Willamette Family Weekend",
    "neighborhood": "Ward 7",
    "price": 255.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 1,
    "name": "Room in boarding house, very centrally located!",
    "neighborhood": "Ward 2",
    "price": 37.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 1,
    "name": "King Bed with Private Bathroom",
    "neighborhood": "Ward 8",
    "price": 65.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "name": "Cozy Home West Salem Near Hospitals Pet Friendly",
    "neighborhood": "Ward 1",
    "price": 72.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 6,
    "name": "Mountain View Memories",
    "neighborhood": "Ward 8",
    "price": 119.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "Scout- a rustic “cabin” apartment, very fast wifi",
    "neighborhood": "Ward 2",
    "price": 136.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 1,
    "name": "Alluring Room In Salem Ideal For Long Term Stay.",
    "neighborhood": "Ward 3",
    "price": 54.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "name": "Classic Town Home on 50 acres of wetlands",
    "neighborhood": "Ward 4",
    "price": 52.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 6,
    "name": "Peace & Tranquility by the River",
    "neighborhood": "Ward 5",
    "price": 270.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 1,
    "name": "Private Room in Comfort Home",
    "neighborhood": "Ward 7",
    "price": 73.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 4,
    "name": "Great place to relax",
    "neighborhood": "Ward 7",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "BRAND NEW SPACIOUS 1 BED ROOM WITH FIREPLACE",
    "neighborhood": "Ward 3",
    "price": 150.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 1,
    "name": "Warm & Welcoming Room - Downtown",
    "neighborhood": "Ward 1",
    "price": 59.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "name": "Jetted Tub, Live Plants and Earthy Atmosphere!",
    "neighborhood": "Ward 1",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "South Salem 1 bd",
    "neighborhood": "Ward 4",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 6,
    "name": "New! Professionally Designed Salem Home!",
    "neighborhood": "Ward 2",
    "price": 168.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "Cheerful bedroom in conveniently located home",
    "neighborhood": "Ward 7",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 5,
    "name": "Bright & Conveniently Located 3 Bedroom Home",
    "neighborhood": "Ward 7",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "name": "Private bedroom available for **ECLIPSE**",
    "neighborhood": "Ward 2",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Private room"
  }
]
```

---

## [Query 4] High-Rated with Wifi (Price Fixed)
**Engine**: Mongo MQL
**Endpoint**: `/api/dashboard/amenities`

### Full JSON Output
```json
[
  {
    "accommodates": 5,
    "id": 1751672,
    "name": "NE Portland Craftsman",
    "neighborhood": "Rose City Park",
    "price": 340.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 5607847,
    "name": "The East Wing",
    "neighborhood": "Mt. Tabor",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "id": 9200540,
    "name": "3-Level Gem Near OHSU & River Priv Suite Included",
    "neighborhood": "South Portland",
    "price": 170.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 6287392,
    "name": "Waterfront condo in SW Portland",
    "neighborhood": "South Portland",
    "price": 120.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "id": 3075414,
    "name": "Modern 2 Bedroom 2 Bath SE Hawthorne House",
    "neighborhood": "Sunnyside",
    "price": 250.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 6376373,
    "name": "Waterfront Pearl District Condo w/ Bridge Views",
    "neighborhood": "Old Town/Chinatown",
    "price": 80.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 781710,
    "name": "House near Mt Tabor, SE Portland",
    "neighborhood": "Montavilla",
    "price": 147.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 11852482,
    "name": "IndigoBirch: Luxurious Zen Garden Retreat: Hot Tub",
    "neighborhood": "Eastmoreland",
    "price": 174.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "id": 14393103,
    "name": "Family home in the neighborhood of East Moreland",
    "neighborhood": "Eastmoreland",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 8,
    "id": 6991450,
    "name": "Gorgeous craftsman in Sellwood!",
    "neighborhood": "Sellwood-Moreland Improvement League",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "id": 9350743,
    "name": "Laurelhurst Gem! Lovely bright 2 bedroom home",
    "neighborhood": "Kerns",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "id": 3821966,
    "name": "Humboldt Apartment",
    "neighborhood": "Overlook",
    "price": 89.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 9276925,
    "name": "Lovely FURNISHED riverfront condo",
    "neighborhood": "Pearl",
    "price": 167.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 4648534,
    "name": "The perfect spot!",
    "neighborhood": "Sellwood-Moreland Improvement League",
    "price": 75.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 13750038,
    "name": "Beautiful Pearl District Loft with On-Site Parking",
    "neighborhood": "Pearl",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "id": 2349023,
    "name": "Cozy Williams Ave Victorian.   Walk to Everything!",
    "neighborhood": "Boise",
    "price": 165.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "id": 8989294,
    "name": "Portland House with Sunset View",
    "neighborhood": "Forest Park",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "id": 9736647,
    "name": "Sunnyside Sanctuary_Belmont/Hawthorne/Laurelhurst",
    "neighborhood": "Sunnyside",
    "price": 300.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 9905408,
    "name": "Nan's North Portland Crepe Myrtle Cottage",
    "neighborhood": "Boise",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 921597,
    "name": "Pearl District Loft: Urban Oasis",
    "neighborhood": "Pearl",
    "price": 99.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "id": 14789940,
    "name": "Cozy and Bright Roseway Heights Cottage",
    "neighborhood": "Rose City Park",
    "price": 111.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 5394124,
    "name": "Beautiful Mt Tabor Home with Mt Hood View - 2b/2b",
    "neighborhood": "Mt. Tabor",
    "price": 250.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 15042822,
    "name": "Historic Portland Charm with Modern Comforts",
    "neighborhood": "Overlook",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 7650094,
    "name": "99 Walk Score | NW Home for Long-Term Stays",
    "neighborhood": "Northwest District",
    "price": 107.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 10596867,
    "name": "Clean, Modern Townhouse w/ Patio in walkable area",
    "neighborhood": "Buckman",
    "price": 136.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 6,
    "id": 12900085,
    "name": "Quiet Neighborhood near Glendoveer and airport",
    "neighborhood": "Wilkes",
    "price": 135.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "id": 557948,
    "name": "Pretty house, perfect location, EV-friendly",
    "neighborhood": "Hosford-Abernethy",
    "price": 721.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "id": 12970336,
    "name": "Spacious modern and private in Alberta Arts Area",
    "neighborhood": "Concordia",
    "price": 117.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 61893,
    "name": "Perfect Portland Place",
    "neighborhood": "Goose Hollow",
    "price": 130.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 15252541,
    "name": "Chic modern apartment in heart of Pearl District",
    "neighborhood": "Pearl",
    "price": 133.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 4054099,
    "name": "Modern Reed College Apartment",
    "neighborhood": "Reed",
    "price": 133.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 13627002,
    "name": "Room in peaceful Montavilla home , private bath",
    "neighborhood": "Montavilla",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 1,
    "id": 697115,
    "name": "Classic Bedroom/Private Vanity",
    "neighborhood": "Hillsdale",
    "price": 56.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "id": 15285983,
    "name": "Portland Peaceful and Friendly Oasis",
    "neighborhood": "Creston-Kenilworth",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "id": 2660141,
    "name": "Portland Bungalow, A Happy House",
    "neighborhood": "Vernon",
    "price": 69.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 4,
    "id": 12223710,
    "name": "Elegant, Modern Garden House",
    "neighborhood": "Mt. Tabor",
    "price": 200.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 8813922,
    "name": "Modern Guest House - Concordia",
    "neighborhood": "Concordia",
    "price": 94.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 5,
    "id": 12375526,
    "name": "Spacious Home, HUGE Yard, 10 Mins to PDX Airport",
    "neighborhood": "Parkrose Heights",
    "price": 259.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 7769491,
    "name": "Minimalist Basement Unit in Historic Irvington",
    "neighborhood": "Irvington",
    "price": 134.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 11669364,
    "name": "Bright Studio in Historic Brooklyn (Inner SE)",
    "neighborhood": "Brooklyn Action Corps",
    "price": 73.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 8130593,
    "name": "Modern 2 bdrm Suites by River, OHSU, downtown",
    "neighborhood": "South Portland",
    "price": 82.0,
    "rating": 5.0,
    "room_type": "Private room"
  },
  {
    "accommodates": 2,
    "id": 15308248,
    "name": "Comfortable & convenient.",
    "neighborhood": "Foster-Powell",
    "price": 150.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 7039107,
    "name": "Sunny, Private, Elegant---Pet Friendly",
    "neighborhood": "Piedmont",
    "price": 99.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 10230029,
    "name": "Cozy Studio In the Woods",
    "neighborhood": "Arnold Creek",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 15500919,
    "name": "The Ladd - A Perfect Walkable Spot",
    "neighborhood": "Hosford-Abernethy",
    "price": 150.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 15414261,
    "name": "Unparalleled City & Mtn Views",
    "neighborhood": "Southwest Hills",
    "price": 158.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 4,
    "id": 15113378,
    "name": "Views, close to OHSU and PSU.  Parking included.",
    "neighborhood": "Portland Downtown",
    "price": 132.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "id": 13869890,
    "name": "Charming sunny 2 BR house in Sellwood",
    "neighborhood": "Sellwood-Moreland Improvement League",
    "price": 0.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 3,
    "id": 6811607,
    "name": "LUX Lava Lounge in downtown Kenton.",
    "neighborhood": "Kenton",
    "price": 86.0,
    "rating": 5.0,
    "room_type": "Entire home/apt"
  },
  {
    "accommodates": 2,
    "id": 1641774,
    "name": "Walk to OHSU/15-min drive to Intel. Pristine Room!",
    "neighborhood": "Hillsdale",
    "price": 60.0,
    "rating": 5.0,
    "room_type": "Private room"
  }
]
```

---

## [Query 5] Historical Review Growth (City Join Fixed)
**Engine**: BigQuery SQL
**Endpoint**: `/api/analysis/review_trends`

### Full JSON Output
```json
[
  {
    "city": "Los Angeles",
    "review_count": 24984,
    "year": 2024
  },
  {
    "city": "Los Angeles",
    "review_count": 19236,
    "year": 2023
  },
  {
    "city": "Los Angeles",
    "review_count": 14926,
    "year": 2022
  },
  {
    "city": "Los Angeles",
    "review_count": 13891,
    "year": 2021
  },
  {
    "city": "Los Angeles",
    "review_count": 6490,
    "year": 2020
  },
  {
    "city": "Los Angeles",
    "review_count": 12028,
    "year": 2019
  },
  {
    "city": "Los Angeles",
    "review_count": 9488,
    "year": 2018
  },
  {
    "city": "Los Angeles",
    "review_count": 6130,
    "year": 2017
  },
  {
    "city": "Los Angeles",
    "review_count": 3481,
    "year": 2016
  },
  {
    "city": "Los Angeles",
    "review_count": 2247,
    "year": 2015
  },
  {
    "city": "Los Angeles",
    "review_count": 1038,
    "year": 2014
  },
  {
    "city": "Los Angeles",
    "review_count": 465,
    "year": 2013
  },
  {
    "city": "Los Angeles",
    "review_count": 175,
    "year": 2012
  },
  {
    "city": "Los Angeles",
    "review_count": 65,
    "year": 2011
  },
  {
    "city": "Los Angeles",
    "review_count": 9,
    "year": 2010
  },
  {
    "city": "Los Angeles",
    "review_count": 1,
    "year": 2009
  },
  {
    "city": "Portland",
    "review_count": 9626,
    "year": 2024
  },
  {
    "city": "Portland",
    "review_count": 7818,
    "year": 2023
  },
  {
    "city": "Portland",
    "review_count": 6820,
    "year": 2022
  },
  {
    "city": "Portland",
    "review_count": 7798,
    "year": 2021
  },
  {
    "city": "Portland",
    "review_count": 4136,
    "year": 2020
  },
  {
    "city": "Portland",
    "review_count": 6902,
    "year": 2019
  },
  {
    "city": "Portland",
    "review_count": 5568,
    "year": 2018
  },
  {
    "city": "Portland",
    "review_count": 3642,
    "year": 2017
  },
  {
    "city": "Portland",
    "review_count": 2150,
    "year": 2016
  },
  {
    "city": "Portland",
    "review_count": 1312,
    "year": 2015
  },
  {
    "city": "Portland",
    "review_count": 566,
    "year": 2014
  },
  {
    "city": "Portland",
    "review_count": 264,
    "year": 2013
  },
  {
    "city": "Portland",
    "review_count": 102,
    "year": 2012
  },
  {
    "city": "Portland",
    "review_count": 14,
    "year": 2011
  },
  {
    "city": "Portland",
    "review_count": 4,
    "year": 2010
  },
  {
    "city": "San Diego",
    "review_count": 11950,
    "year": 2024
  },
  {
    "city": "San Diego",
    "review_count": 9882,
    "year": 2023
  },
  {
    "city": "San Diego",
    "review_count": 7267,
    "year": 2022
  },
  {
    "city": "San Diego",
    "review_count": 7095,
    "year": 2021
  },
  {
    "city": "San Diego",
    "review_count": 3629,
    "year": 2020
  },
  {
    "city": "San Diego",
    "review_count": 4551,
    "year": 2019
  },
  {
    "city": "San Diego",
    "review_count": 3541,
    "year": 2018
  },
  {
    "city": "San Diego",
    "review_count": 2156,
    "year": 2017
  },
  {
    "city": "San Diego",
    "review_count": 1295,
    "year": 2016
  },
  {
    "city": "San Diego",
    "review_count": 696,
    "year": 2015
  },
  {
    "city": "San Diego",
    "review_count": 293,
    "year": 2014
  },
  {
    "city": "San Diego",
    "review_count": 126,
    "year": 2013
  },
  {
    "city": "San Diego",
    "review_count": 34,
    "year": 2012
  },
  {
    "city": "San Diego",
    "review_count": 11,
    "year": 2011
  },
  {
    "city": "San Diego",
    "review_count": 4,
    "year": 2010
  }
]
```

---

## [Query 6] BigQuery: Market Stats (NaN Handled)
**Engine**: BigQuery SQL
**Endpoint**: `/api/analysis/market_stats`

### Full JSON Output
```json
[
  {
    "avg_price": 0,
    "city": "San Diego",
    "neighborhood": "Mission Bay",
    "total_listings": 1886
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Long Beach",
    "total_listings": 1858
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Hollywood",
    "total_listings": 1816
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Venice",
    "total_listings": 1540
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Santa Monica",
    "total_listings": 1244
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "West Hollywood",
    "total_listings": 1220
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Downtown",
    "total_listings": 1187
  },
  {
    "avg_price": 0,
    "city": "San Diego",
    "neighborhood": "Pacific Beach",
    "total_listings": 1060
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Beverly Hills",
    "total_listings": 1055
  },
  {
    "avg_price": 0,
    "city": "San Diego",
    "neighborhood": "La Jolla",
    "total_listings": 1017
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Pasadena",
    "total_listings": 778
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Glendale",
    "total_listings": 731
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Alhambra",
    "total_listings": 729
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Hollywood Hills",
    "total_listings": 727
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Hollywood Hills West",
    "total_listings": 676
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Exposition Park",
    "total_listings": 654
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Culver City",
    "total_listings": 641
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Rowland Heights",
    "total_listings": 626
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Burbank",
    "total_listings": 616
  },
  {
    "avg_price": 0,
    "city": "San Diego",
    "neighborhood": "Ocean Beach",
    "total_listings": 608
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Koreatown",
    "total_listings": 603
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Mid-City",
    "total_listings": 587
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Beverly Grove",
    "total_listings": 577
  },
  {
    "avg_price": 0,
    "city": "San Diego",
    "neighborhood": "North Hills",
    "total_listings": 554
  },
  {
    "avg_price": 0,
    "city": "San Diego",
    "neighborhood": "East Village",
    "total_listings": 552
  },
  {
    "avg_price": 0,
    "city": "San Diego",
    "neighborhood": "Midtown",
    "total_listings": 550
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Woodland Hills",
    "total_listings": 538
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Westlake",
    "total_listings": 537
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Sherman Oaks",
    "total_listings": 525
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Mid-Wilshire",
    "total_listings": 521
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Westwood",
    "total_listings": 505
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Silver Lake",
    "total_listings": 494
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "North Hollywood",
    "total_listings": 490
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Redondo Beach",
    "total_listings": 465
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Inglewood",
    "total_listings": 460
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Malibu",
    "total_listings": 445
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Manhattan Beach",
    "total_listings": 435
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Marina del Rey",
    "total_listings": 406
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Sawtelle",
    "total_listings": 403
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Topanga",
    "total_listings": 387
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "East Hollywood",
    "total_listings": 385
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Lancaster",
    "total_listings": 385
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Studio City",
    "total_listings": 384
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "East Los Angeles",
    "total_listings": 377
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Torrance",
    "total_listings": 372
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Echo Park",
    "total_listings": 372
  },
  {
    "avg_price": 0,
    "city": "San Diego",
    "neighborhood": "Loma Portal",
    "total_listings": 367
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Santa Clarita",
    "total_listings": 349
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Hacienda Heights",
    "total_listings": 342
  },
  {
    "avg_price": 0,
    "city": "Los Angeles",
    "neighborhood": "Monterey Park",
    "total_listings": 332
  }
]
```

---


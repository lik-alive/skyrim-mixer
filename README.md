# Skyrim-Mixer

## Info

**Helper for Skyrim Alchemy**

This mini-service is very useful for discovering alchemical effects in The Elder Scrolls V Skyrim by effectively mixing the appropriate ingredients. It is fast, simple and extremely easy to use on any device to support your playthrough.

## Table of Contents
- [Features](#features)
  - [Common](#common)
  - [Functionality](#functionality)
- [Installation](#installation)
  - [For development](#for-development)
  - [For production](#for-production)
- [License](#license)

## Features

### Common
- Python v3.10 HTTP server
- jQuery v3.4.1
- Bootstrap v4.4.1
- DB: Inline Python Dictionary
- Mobile-friendly
- Dockerized

### Functionality
- Fast search
- Effective mixes (reveal 1, 2 or 3 effects at once)
- Matching ingredients for each effect

## Installation

### For development

1. Create `.env`

2. Deploy
```sh
./deploy.sh
```

### For production

1. Create `.env`

2. Deploy
```sh
./deploy.sh --prod
```

## License

MIT License
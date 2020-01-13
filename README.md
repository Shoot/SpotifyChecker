# SpotifyChecker
Credential stuffing program for Spotify that automatically gets the `__bon` cookie. This program was made for educational purposes only. I am not responsible for what you use this for.

## Getting Started
### Prerequisites
- Python 3

### Installing
Clone the latest version of this repository to a folder with the following command.
```
git clone https://github.com/Shoot/FMSquared.git
```
Once you've cloned the repository, install the requirements from `requirements.txt` using `pip install -r requirements.txt`.

## Usage
1. Make a new file called `list.txt`, inside it put your data with the format `user:pass` on each line.
2. Run the program by typing `py main.py`.

From here, it will check each combination and output any successful results into `out <current time in seconds since epoch>.txt`.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Shoot/SpotifyChecker/blob/master/LICENSE) file for details.
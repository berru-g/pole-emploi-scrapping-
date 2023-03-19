/*Learn python
github/berru-g 23*/
import { sleep } from 'pyautogui';
import * as requests from 'requests';
import { BeautifulSoup } from 'bs4';
import * as smtplib from 'smtplib';
import { MIMEText } from 'email/mime/text';
import { MIMEMultipart } from 'email/mime/multipart';
import * as os from 'os';
var dates, indeed_search, indeed_soup, indeed_titles, indeed_url, jeudisdotcom_search, jeudisdotcom_soup, jeudisdotcom_titles, jeudisdotcom_url, job, location, nom_script, poleemploi_search, poleemploi_soup, poleemploi_titles, poleemploi_url, reponse, subtitles;
console.log("Entrez le titre du poste:");
job = input("");
console.log("Entrez l emplacement:");
location = input("");
poleemploi_url = "https://candidat.pole-emploi.fr/offres/recherche?&motsCles={}&lieux{}&offresPartenaires=true&rayon=10&tri=0";
jeudisdotcom_url = "https://www.lesjeudis.com/recherche?keywords={}&location={}";
indeed_url = "https://fr.indeed.com/emplois?q={}&l={}&vjk=52ed5b81115cbba2";
poleemploi_search = requests.get(poleemploi_url.format(job, location));
poleemploi_soup = new BeautifulSoup(poleemploi_search.text, "html.parser");
poleemploi_titles = poleemploi_soup.find_all({
  "class_": "media-heading-title"
});
subtitles = poleemploi_soup.find_all({
  "class_": "subtext"
});
dates = poleemploi_soup.find_all({
  "class_": "date"
});
console.log("R\u00e9sultats de la recherche sur Pole Emploi:");

for (var title, _pj_c = 0, _pj_a = poleemploi_titles, _pj_b = _pj_a.length; _pj_c < _pj_b; _pj_c += 1) {
  title = _pj_a[_pj_c];

  for (var subtitle, _pj_f = 0, _pj_d = subtitles, _pj_e = _pj_d.length; _pj_f < _pj_e; _pj_f += 1) {
    subtitle = _pj_d[_pj_f];

    for (var date, _pj_i = 0, _pj_g = dates, _pj_h = _pj_g.length; _pj_i < _pj_h; _pj_i += 1) {
      date = _pj_g[_pj_i];
      console.log(title.text);
      console.log(subtitle.text);
      console.log(date.text);
      console.log("__________");
    }
  }
}

sleep(1);
jeudisdotcom_search = requests.get(jeudisdotcom_url.format(job, location));
jeudisdotcom_soup = new BeautifulSoup(jeudisdotcom_search.text, "html.parser");
jeudisdotcom_titles = jeudisdotcom_soup.find_all({
  "class_": ["data-results-title.dark-blue-text.b", "data-results-content block job-listing-item"]
});
console.log("R\u00e9sultats de la recherche sur jeudis.com:");

for (var title, _pj_c = 0, _pj_a = jeudisdotcom_titles, _pj_b = _pj_a.length; _pj_c < _pj_b; _pj_c += 1) {
  title = _pj_a[_pj_c];
  console.log(title.text);
}

sleep(1);
indeed_search = requests.get(indeed_url.format(job, location));
indeed_soup = new BeautifulSoup(indeed_search.text, "html.parser");
indeed_titles = indeed_soup.find_all({
  "id_": ["jobTitle-37b88858c4da5049", "jobTitle css-1h4a4n5 eu4oa1w0"]
});
console.log("R\u00e9sultats de la recherche sur Indeed.com:");

for (var title, _pj_c = 0, _pj_a = indeed_titles, _pj_b = _pj_a.length; _pj_c < _pj_b; _pj_c += 1) {
  title = _pj_a[_pj_c];
  console.log(title.text);
}

sleep(1);
console.log("Fin des r\u00e9sultats");
console.log("Voulez-vous envoyer un mail group\u00e9 oui/non ?");
reponse = input();

if (reponse.lower() === "oui") {
  nom_script = "reponse-mail-auto.py";

  if (os.path.isfile(nom_script)) {
    os.system("python " + nom_script);
  } else {
    console.log("Le script rencontre un probleme.");
  }
} else {
  if (reponse.lower() === "non") {
    console.log("Merci d'avoir utilis\u00e9 notre programme.");
    console.log("Aidez nous \u00e0 am\u00e9liorer cet outil, rdv sur github.com/berru-g");
    exit();
  }
}

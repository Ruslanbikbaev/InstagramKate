$instagram = new \InstagramScraper\Instagram(new \GuzzleHttp\Client());
$nonPrivateAccountMedias = $instagram->getMedias('kevin');
echo $nonPrivateAccountMedias[0]->getLink();

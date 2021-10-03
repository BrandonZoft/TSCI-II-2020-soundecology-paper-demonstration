# librerias
library(tuneR)
library(seewave)
library(soundecology)

# genera csv del sitio de manzanillo forest.
multiple_sounds('sites/manzanillo_forest/', "sites/manzanillo_forest_results_acoustic_complexity_index_ACI.csv", soundindex = "acoustic_complexity", max_freq = 11025)
multiple_sounds('sites/manzanillo_forest/', "sites/manzanillo_forest_results_bioacoustic_index_BIO.csv", soundindex = "bioacoustic_index", min_freq = 2000, max_freq = 8000)
multiple_sounds('sites/manzanillo_forest/', "sites/manzanillo_forest_results_acoustic_entropy_H.csv", soundindex = "H")
multiple_sounds('sites/manzanillo_forest/', "sites/manzanillo_forest_results_acoustic_diversity_ADI.csv", soundindex = "acoustic_diversity", max_freq=10000, db_threshold=-50)
multiple_sounds('sites/manzanillo_forest/', "sites/manzanillo_forest_results_acoustic_evenness_AEI.csv", soundindex = "acoustic_evenness", max_freq=10000, db_threshold=-50)
multiple_sounds('sites/manzanillo_forest/', "sites/manzanillo_forest_results_ndsi.csv", soundindex = "ndsi", anthro_min = 1000, anthro_max = 2000, bio_min = 2000, bio_max = 11025)

# genera csv del sitio de caribbean coast.
multiple_sounds('sites/caribbean_coast/', "sites/caribbean_coast_results_acoustic_complexity_index_ACI.csv", soundindex = "acoustic_complexity", max_freq = 11025)
multiple_sounds('sites/caribbean_coast/', "sites/caribbean_coast_results_bioacoustic_index_BIO.csv", soundindex = "bioacoustic_index", min_freq = 2000, max_freq = 8000)
multiple_sounds('sites/caribbean_coast/', "sites/caribbean_coast_results_acoustic_entropy_H.csv", soundindex = "H")
multiple_sounds('sites/caribbean_coast/', "sites/caribbean_coast_results_acoustic_diversity_ADI.csv", soundindex = "acoustic_diversity", max_freq=10000, db_threshold=-50)
multiple_sounds('sites/caribbean_coast/', "sites/caribbean_coast_results_acoustic_evenness_AEI.csv", soundindex = "acoustic_evenness", max_freq=10000, db_threshold=-50)
multiple_sounds('sites/caribbean_coast/', "sites/caribbean_coast_results_ndsi.csv", soundindex = "ndsi", anthro_min = 1000, anthro_max = 2000, bio_min = 2000, bio_max = 11025)

# genera csv del sitio de blanco national park.
multiple_sounds('sites/blanco_national_park/', "sites/blanco_national_park_results_acoustic_complexity_index_ACI.csv", soundindex = "acoustic_complexity", max_freq = 11025)
multiple_sounds('sites/blanco_national_park/', "sites/blanco_national_park_results_bioacoustic_index_BIO.csv", soundindex = "bioacoustic_index", min_freq = 2000, max_freq = 8000)
multiple_sounds('sites/blanco_national_park/', "sites/blanco_national_park_results_acoustic_entropy_H.csv", soundindex = "H")
multiple_sounds('sites/blanco_national_park/', "sites/blanco_national_park_results_acoustic_diversity_ADI.csv", soundindex = "acoustic_diversity", max_freq=10000, db_threshold=-50)
multiple_sounds('sites/blanco_national_park/', "sites/blanco_national_park_results_acoustic_evenness_AEI.csv", soundindex = "acoustic_evenness", max_freq=10000, db_threshold=-50)
multiple_sounds('sites/blanco_national_park/', "sites/blanco_national_park_results_ndsi.csv", soundindex = "ndsi", anthro_min = 1000, anthro_max = 2000, bio_min = 2000, bio_max = 11025)
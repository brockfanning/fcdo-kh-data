from sdg.open_sdg import open_sdg_build
from alter_meta import alter_meta

open_sdg_build(config='config_data.yml',
               alter_meta=alter_meta)

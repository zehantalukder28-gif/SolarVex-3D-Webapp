import os
import glob
import shutil

src_dir = r"C:\Users\Admin\.gemini\antigravity\brain\60bbcc27-2c38-48fd-b973-2ebeeb01730e"
dest_dir = r"c:\Users\Admin\Downloads\Works whm\SolarVex-webapp-main\SolarVex-webapp-main\images"

patterns = {
    "hero_editorial_*.png": "hero-bg.jpg",
    "pv_system_editorial_*.png": "pv-system.jpg",
    "energy_storage_editorial_*.png": "energy-storage.jpg",
    "ev_charger_editorial_*.png": "ev-charger.jpg",
    "smart_energy_editorial_*.png": "smart-energy.jpg",
    "solar_farm_editorial_*.png": "solar-farm.jpg"
}

for pattern, new_name in patterns.items():
    matches = glob.glob(os.path.join(src_dir, pattern))
    if matches:
        latest_file = max(matches, key=os.path.getctime)
        dest_path = os.path.join(dest_dir, new_name)
        shutil.copy2(latest_file, dest_path)
        print(f"OK: {new_name}")
    else:
        print(f"MISS: {pattern}")

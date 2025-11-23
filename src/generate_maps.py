import os
from prettymapp.geo import get_aoi
from prettymapp.osm import get_osm_geometries
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES
import matplotlib.pyplot as plt

# 设置保存路径到桌面，确保你能找到
desktop_path = os.path.expanduser("~/Desktop/Final_Maps_Output")
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)

print(f"------------\n图片将保存到这里: {desktop_path}\n------------")

# 关键修改：直接使用经纬度 (Latitude, Longitude)，跳过联网查询地名的步骤
# 格式: (纬度, 经度)
SPECIES_LOCATIONS = {
    "Giant_Panda": (31.03, 103.19),  # 卧龙
    "Yangtze_Finless_Porpoise": (29.13, 116.23), # 鄱阳湖
    "South_China_Tiger": (25.28, 116.88), # 梅花山
    "Golden_Snub_nosed_Monkey": (31.74, 110.67), # 神农架
    "Crested_Ibis": (33.22, 107.54), # 洋县
    "Snow_Leopard": (34.00, 93.00), # 三江源 (大概中心)
    "Tibetan_Antelope": (35.00, 90.00), # 可可西里
    "Asian_Elephant": (21.92, 101.25), # 西双版纳
    "Hainan_Gibbon": (19.10, 109.10) # 霸王岭
}

def generate_habitat_map(species_name, coordinates, style_name="Peach"):
    try:
        print(f"正在生成: {species_name} (坐标: {coordinates})...")
        
        # 修改点：使用 coordinates 参数而不是 address
        aoi = get_aoi(coordinates=coordinates, radius=3000, rectangular=False)
        
        # 获取地图数据
        df = get_osm_geometries(aoi=aoi)
        
        # 绘图
        fig = Plot(
            df=df,
            aoi_bounds=aoi.bounds,
            draw_settings=STYLES[style_name],
            shape="circle",
        ).plot_all()
        
        # 保存
        output_path = os.path.join(desktop_path, f"{species_name}.png")
        fig.savefig(output_path)
        print(f"✅ 成功保存! -> {output_path}")
        
    except Exception as e:
        print(f"❌ 生成失败 {species_name}: {e}")

if __name__ == "__main__":
    for species, coords in SPECIES_LOCATIONS.items():
        # 轮换一下颜色风格
        style = "Auburn" if len(species) % 2 == 0 else "Peach"
        generate_habitat_map(species, coords, style)
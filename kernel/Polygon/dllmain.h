// dllmain.h : 모듈 클래스의 선언입니다.

class CPolygonModule : public ATL::CAtlDllModuleT< CPolygonModule >
{
public :
	DECLARE_LIBID(LIBID_PolygonLib)
	DECLARE_REGISTRY_APPID_RESOURCEID(IDR_POLYGON, "{71f7c75f-9a11-4ac2-9e1d-e691ffc4a3d3}")
};

extern class CPolygonModule _AtlModule;

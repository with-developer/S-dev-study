// Polygon.cpp : DLL 내보내기 구현입니다.


#include "pch.h"
#include "framework.h"
#include "resource.h"
#include "Polygon_i.h"
#include "dllmain.h"


using namespace ATL;

// DLL이 OLE에 의해 언로드될 수 있는지 결정하는 데 사용됩니다.
_Use_decl_annotations_
STDAPI DllCanUnloadNow(void)
{
	return _AtlModule.DllCanUnloadNow();
}

// 클래스 팩터리를 반환하여 요청된 형식의 개체를 만듭니다.
_Use_decl_annotations_
STDAPI DllGetClassObject(_In_ REFCLSID rclsid, _In_ REFIID riid, _Outptr_ LPVOID* ppv)
{
	return _AtlModule.DllGetClassObject(rclsid, riid, ppv);
}

// DllRegisterServer - 시스템 레지스트리에 항목을 추가합니다.
_Use_decl_annotations_
STDAPI DllRegisterServer(void)
{
	// 개체, typelib 및 typelib에 들어 있는 모든 인터페이스를 등록합니다.
	HRESULT hr = _AtlModule.DllRegisterServer();
	return hr;
}

// DllUnregisterServer - 시스템 레지스트리에서 항목을 제거합니다.
_Use_decl_annotations_
STDAPI DllUnregisterServer(void)
{
	HRESULT hr = _AtlModule.DllUnregisterServer();
	return hr;
}

// DllInstall - 항목을 사용자별 및 컴퓨터별로 시스템 레지스트리에 추가하거나 시스템 레지스트리에서 제거합니다.
STDAPI DllInstall(BOOL bInstall, _In_opt_  LPCWSTR pszCmdLine)
{
	HRESULT hr = E_FAIL;
	static const wchar_t szUserSwitch[] = L"user";

	if (pszCmdLine != nullptr)
	{
		if (_wcsnicmp(pszCmdLine, szUserSwitch, _countof(szUserSwitch)) == 0)
		{
			ATL::AtlSetPerUserRegistration(true);
		}
	}

	if (bInstall)
	{
		hr = DllRegisterServer();
		if (FAILED(hr))
		{
			DllUnregisterServer();
		}
	}
	else
	{
		hr = DllUnregisterServer();
	}

	return hr;
}



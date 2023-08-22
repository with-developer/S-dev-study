#pragma once

using namespace ATL;

template <class T>
class CProxy_IATLControlEvents : public IConnectionPointImpl<T, &__uuidof(_IATLControlEvents), CComDynamicUnkArray>
{
	// 경고: 해당 마법사에서 이 클래스를 다시 생성할 수도 있습니다.
public:
};

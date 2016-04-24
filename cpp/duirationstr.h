#ifndef CPP_UTILITIES_DUIRATIONSTR_H_
#define CPP_UTILITIES_DUIRATIONSTR_H_

#include <string>
#include <chrono>

namespace XDUtil {

/**
 * @brief  convert duration to stream.
 *
 * @tparam V
 * @tparam R
 * @param d the duration to convert.
 *
 * @returns   the string represent of the duration
 */
template <typename V, typename R>
std::string DurationStr(const std::chrono::duration<V, R>& d) {
    return std::string("[" + std::to_string(d.count()) + " of " +
                       std::to_string(R::num) + std::to_string(R::den) + "]");
}

/**
 * @brief  print the duration to ostream
 */
template <typename V, typename R>
std::ostream& operator<<(std::ostream& s,
                         const std::chrono::duration<V, R>& d) {
    return s << DurationStr(d);
}

}  // XDUtil

#endif /* end of include guard: CPP_UTILITIES_DUIRATIONSTR_H_ */

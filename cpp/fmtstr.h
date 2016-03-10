#ifndef CPP_UTILITIES_FMTSTR_H_
#define CPP_UTILITIES_FMTSTR_H

#include <string>

using std::string;

/**
 * @brief  A python style string format function. i.e.
 *
 *           FormatString("{} world, PI is {}", "hello", 3.1415)
 *
 *         will give you
 *
 *           "hello world, PI is 3.1415"
 *
 *         If there are more values than placehoder(i.e. "{}"), remain
 *         values will be throwed away.
 *
 *           FormatString("{} world, PI is", "hello", 3.1415)
 *
 *         will give you
 *
 *           "hello world, PI is"
 *
 *         If there are more placehoder than values, placehoder will be
 *         preserved.
 *
 *           FormatString("{} world, PI is {}", "hello")
 *
 *         while give you
 *
 *           "hello world, PI is {}"
 *
 *         This function use c++11 new feature -- variadic template,
 *         so you will need c++11 compiler to use it
 *
 * @param fmt_spec format specification that use "{}" as placeholder
 * @param args values corresponding to "{}" in previous specification
 *
 * @returns new string that replace all "{}" with its corresponding value
 */
template <typename... Types>
const std::string FormatString(const std::string& fmt_spec,
                               const Types&... args);

#include "fmtstr.cpp"

#endif /* end of include guard: CPP_UTILITIES_FMTSTR_H_ */

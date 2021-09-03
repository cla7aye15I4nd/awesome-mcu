## CVE-2021-31572

- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31572
- https://github.com/FreeRTOS/FreeRTOS-Kernel/pull/226/files

Add addition overflow check for stream buffer for the mostly theoretical case where you are allocating close to 4,294,967,296 bytes and the size_t rolls over.

Overflow happed when `size_t xBufferSizeBytes > 2^32 -  sizeof(StreamBuffer_t)`

```c
xBufferSizeBytes++;
pucAllocatedMemory = ( uint8_t * ) pvPortMalloc( xBufferSizeBytes + sizeof( StreamBuffer_t ) ); /*lint !e9079 malloc() only returns void*. */
```

```c
if( xBufferSizeBytes < ( xBufferSizeBytes + 1 + sizeof( StreamBuffer_t ) ) )
{
    xBufferSizeBytes++;
    pucAllocatedMemory = ( uint8_t * ) pvPortMalloc( xBufferSizeBytes + sizeof( StreamBuffer_t ) ); /*lint !e9079 malloc() only returns void*. */
}
else
{
    pucAllocatedMemory = NULL;
}
```

